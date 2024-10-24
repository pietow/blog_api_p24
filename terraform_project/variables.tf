# Define variables for reuse and flexibility

variable "ec2_instance_type" {
  default = "t3.micro"
}

variable "rds_username" {
  type        = string
  description = "Username for RDS"
}

variable "rds_password" {
  type        = string
  description = "Password for RDS"
  sensitive   = true
}

