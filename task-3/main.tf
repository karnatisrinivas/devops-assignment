provider "aws" {
  region = "us-east-1"
}

variable "ami_id" {
  default = "ami-0c843a5f56de7b928"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "SSH key pair"
  default     = "srini-veris"
}

variable "subnet_ids" {
  description = "List of subnet IDs"
  type        = list(string)
  default     = ["subnet-0fae32127637c0b6f", "subnet-0b9bf78b7abc9d76b"]
}

variable "security_group_id" {
  description = "The security group ID for the instances"
  default     = "sg-07d922a4d7e248ad6"
}

resource "aws_launch_configuration" "veris_launch_configuration" {
  name             = "veris-launch-configuration"
  image_id         = var.ami_id
  instance_type    = var.instance_type
  key_name         = var.key_name
  security_groups  = [var.security_group_id]

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "veris_asg" {
  launch_configuration = aws_launch_configuration.veris_launch_configuration.id
  min_size             = 1
  max_size             = 3
  desired_capacity     = 1
  vpc_zone_identifier  = var.subnet_ids
  health_check_type    = "EC2"
  health_check_grace_period = 300

  tag {
    key                 = "Name"
    value               = "veris-asg-instance"
    propagate_at_launch = true
  }
}

output "asg_name" {
  value = aws_autoscaling_group.veris_asg.name
}
