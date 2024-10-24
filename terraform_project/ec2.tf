# Security Group for EC2
resource "aws_security_group" "ec2_sg" {
  vpc_id = aws_vpc.main.id

  # Allow inbound SSH (port 22)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow inbound HTTP (port 80)
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "ec2_sg"
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami                         = "ami-0084a47cc718c111a"  # Replace with appropriate AMI
  instance_type               = var.ec2_instance_type
  subnet_id                   = aws_subnet.public.id
  vpc_security_group_ids         = [aws_security_group.ec2_sg.id]
  associate_public_ip_address = true

# User data script to install PostgreSQL client and Docker
  user_data = <<-EOF
              #!/bin/bash

              # Update the package list
              sudo apt update -y

              # Install PostgreSQL client for Ubuntu
              sudo apt install -y postgresql-client

              # Installing Docker on Ubuntu

              # 1. Install required dependencies
              sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

              # 2. Add the Docker repository
              curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
              sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

              # 3. Update the package list again
              sudo apt update -y

              # 4. Install Docker CE (Community Edition)
              sudo apt install -y docker-ce docker-ce-cli containerd.io

              # Ensure Docker starts on boot
              sudo systemctl enable docker
              sudo systemctl start docker
              EOF

  tags = {
    Name = "web_instance"
  }
}
