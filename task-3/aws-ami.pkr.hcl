packer {
  required_plugins {
    amazon = {
      version = ">= 0.0.1"
      source  = "github.com/hashicorp/amazon"
    }
    ansible = {
      version = "~> 1"
      source = "github.com/hashicorp/ansible"
    }

  }
}

source "amazon-ebs" "example" {
  ami_name      = "My AMI"
  instance_type = "t2.micro"
  region        = "us-east-1"
  ssh_username  = "ec2-user"
  source_ami    = "ami-0eaf7c3456e7b5b68"
}

build {
  sources = ["source.amazon-ebs.example"]
  provisioner  "shell" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y python3",
      "sudo yum install -y python3-pip",
      "sudo pip3 install ansible",
    ]
  }
  provisioner "ansible" {
    playbook_file = "./playbook.yml"
    user          = "ec2-user"
  }
 
}