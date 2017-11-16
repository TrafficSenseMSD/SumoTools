import shutil
import os

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    print("Building sumo_tools packages")
    src_files = os.listdir('sumo/tools')

    shutil.rmtree('sumotools', ignore_errors=True)
    os.mkdir('sumotools')
    open('sumotools/__init__.py', 'w').close()
    shutil.copytree('sumo/tools/sumolib', 'sumotools/sumolib')

    shutil.copytree('sumo/tools/traci', 'sumotools/traci')

    os.mkdir('sumotools/scripts')

    shutil.copytree('sumo/tools/shapes', 'sumotools/scripts/shapes/')
    #open('scripts/shapes/__init__.py', 'w').close()

    shutil.copytree('sumo/tools/xml', 'sumotools/scripts/xml/')

    shutil.copytree('sumo/tools/visualization', 'sumotools/scripts/visualization/')
    shutil.copytree('sumo/tools/output', 'sumotools/scripts/output/')



if __name__ == "__main__":
    main()