pipeline {
    agent any

    parameters {
        string(name: 'Operand1', defaultValue: '0', description: 'First operand')
        string(name: 'Operand2', defaultValue: '0', description: 'Second operand')
        choice(name: 'Operation', choices: ['+', '-', '*', '/'], description: 'Operation to perform')
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                checkout scm
            }
        }

        stage('Run Calculator') {
            steps {
                script {
                    // Run the Python script with parameters
                    def command = "python3 calculator.py ${params.Operand1} ${params.Operand2} ${params.Operation}"
                    echo "Executing: ${command}"
                    def result = sh(script: command, returnStdout: true).trim()
                    echo "Result: ${result}"
                }
            }
        }
    }
}
