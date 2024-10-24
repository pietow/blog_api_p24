# Security Group for RDS
resource "aws_security_group" "rds_sg" {
  vpc_id = aws_vpc.main.id

  # Allow PostgreSQL access from EC2
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    security_groups = [aws_security_group.ec2_sg.id]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "rds_sg"
  }
}

# RDS PostgreSQL Instance
resource "aws_db_instance" "postgres" {
  skip_final_snapshot = true
  allocated_storage    = 20
  engine               = "postgres"
  instance_class       = "db.t3.micro"
  db_name                 = "mydb"
  username             = var.rds_username
  password             = var.rds_password
  port                 = 5432
  publicly_accessible  = false
  db_subnet_group_name = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  tags = {
    Name = "rds_postgres"
  }


}

# RDS Subnet Group
resource "aws_db_subnet_group" "main" {
  name       = "main_subnet_group"
  subnet_ids = [aws_subnet.private_a.id, aws_subnet.private_b.id]

  tags = {
    Name = "main_db_subnet_group"
  }
}

