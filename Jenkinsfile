pipeline{
    agent any

    stages{
        stage("testingInstall"){
            steps{
                sh 'echo "installing docker locally"'
                sh 'chmod 775 ./script/*'
                sh './script/before_installation.sh'
            }
        }
        stage("testing docker swarm"){
            steps{
                sh 'echo "install testing docker-swarm"'
                sh 'pip3 install pytest'
                sh 'pip3 install coverage'
                sh 'pip3 install -r /var/lib/jenkins/workspace/pipeline2/requirements.txt'
                sh 'sudo docker swarm init'
                sh 'sudo docker stack deploy --compose-file /var/lib/jenkins/workspace/pipeline2/testing-docker-swarm.yml stackdemo'
                sh 'sleep 30'
                sh 'echo "checking URLs"'
                sh 'python3 -m coverage run --source=. -m pytest test/testing.py'
                sh 'python3 -m coverage report'
                sh 'sudo docker stack rm service stackdemo'
                sh 'sudo docker swarm leave -f'
                sh 'sleep 10'
            }
        }
        stage("installing ansible"){
            steps{
                sh 'sudo apt update'
                sh 'sudo apt install software-properties-common'
                sh 'sudo sudo apt-add-repository --yes --update ppa:ansible/ansible'
                sh 'sudo apt install ansible'
            }
        }
        stage("environment-setting"){
            steps{
                sh 'ansible-playbook -i docker.conf docker-installation.yml'
                sh 'echo "docker install"'
            }
        }
        stage("nodes-assigned"){
            steps{
                sh 'ansible-playbook -i docker.conf assign-nodes.yml'
                sh 'echo "Nodes assigned"'
            }
        }
        stage("depoly-swarm"){
            steps{
                sh 'ansible-playbook -i docker.conf deploy-swarm.yml'
                sh 'echo "swarm depolyed"'
                sh 'sleep 20'
            }
        }
        stage("db-testing"){
            steps{
                sh 'echo "testing db"'
                sh 'chmod 775 ./script/*'
                sh 'pip3 install -r /var/lib/jenkins/workspace/pipeline2/requirements.txt'
                sh 'echo "checking URLs"'
                sh './script/db.sh'
            }
        }
    }
}