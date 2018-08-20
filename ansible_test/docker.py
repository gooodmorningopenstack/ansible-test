import subprocess
import os

def generate_dockerfile(context):
    '''Returns the file path to the rendered Dockerfile'''
    rendered_dockerfile_contents = Template(
        resource_string("ansible_test", "resources/Dockerfile.j2")
    ).render(context)

    rendered_dockerfile_path = os.path.join(os.getcwd(), "Dockerfile")
    with open(rendered_dockerfile_path, "wb") as f:
        f.write(rendered_dockerfile_contents)

    return rendered_dockerfile_path

def build_container():
    subprocess.check_call(
        ['docker', 'build', '-t', CONTAINER_NAME, '.']
    )

def run_container():
    subprocess.check_call(
        [
            'docker', 'run', '-e', 'DOCKER_TEST_ROLE=%s' % args.role,
            '--privileged=true', '-it', CONTAINER_NAME
        ]
    )
