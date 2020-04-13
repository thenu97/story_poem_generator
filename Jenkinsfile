pipeline{
    agent any

    stages{
        stage("Test Install"){
            steps{
                sh 'echo "installing docker locally"'
                sh 'chmod 775 ./scripts/*'
                sh './scripts/before_installation.sh'
            }
        }
        stage("Test Docker Swarm"){
            steps{
                sh 'echo "install testing docker-swarm"'
                sh 'chmod 775 ./scripts/*'
                sh './scripts/installation.sh'
                sh 'sudo docker swarm init'
                sh 'sudo docker stack deploy --compose-file /var/lib/jenkins/workspace/posto/testing-docker-swarm.yml stackdemo'
                sh 'sleep 15'
                sh 'echo "checking URLs"'
                sh './scripts/run_before.sh'
                sh 'sudo docker stack rm service stackdemo'
                sh 'sudo docker swarm leave -f'
                sh 'sleep 10'
            }
        }
        stage("Installing Ansible"){
            steps{
                sh 'sudo apt update'
                sh 'sudo apt install software-properties-common'
                sh 'sudo sudo apt-add-repository --yes --update ppa:ansible/ansible'
                sh 'sudo apt install ansible'
                sh 'echo "all good to go"'
            }
        }
        stage("Environment Setting"){
            steps{
                sh 'echo "installing docker via ansible"'
                sh 'ansible-playbook -i ./ansible/docker.conf ./ansible/docker-installation.yml'
                sh 'echo "docker installed"'
            }
        }
        stage("Nodes Assigned"){
            steps{
                sh 'echo "assigning nodes via ansible"'
                sh 'ansible-playbook -i ./ansible/docker.conf ./ansible/assign-nodes.yml'
                sh 'echo "nodes assigned"'
            }
        }
        stage("Deploy Swarm"){
            steps{
                sh 'echo "deploy docker via ansible"'
                sh 'ansible-playbook -i ./ansible/docker.conf ./ansible/deploy-swarm.yml'
                sh 'echo "swarm depolyed"'
                sh 'sleep 30'
            }
        }
        stage("Testing"){
            steps{
                sh 'echo "testing db"'
                sh 'chmod 775 ./scripts/*'
                sh 'echo "checking URLs"'
                sh './scripts/run_after.sh'
            }
        }
    }
}