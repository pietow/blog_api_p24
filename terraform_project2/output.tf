# Outputs to reference created resources

output "vpc_id" {
    value = aws_vpc.main.id
}

output "ec2_instance_id" {
    value = aws_instance.web.id
}

output "rds_instance_endpoint" {
    value = aws_db_instance.postgres.endpoint
}