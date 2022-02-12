rem I actually don't know yet how to automate the environment creation/upd
rem These command line notes/ snippets that are executed manually 
rem /****************************************************/
rem /***********activate conda **************************/
C:\ProgramData\Miniconda3\Scripts\activate.bat C:\ProgramData\Miniconda3

rem /***********create the environment ******************/
conda env create --prefix C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\song-play-schema-env --file environment.yml

rem /***********activate the environment ******************/
conda activate C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\song-play-schema-env

rem /***********when requirements need updated environment **********/
conda env update --file environment.yml --prune

rem /*********** remove environment if needed  **********/
conda env remove --prefix C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\song-play-schema-env

C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\song-play-schema-env\python C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\db_connection_config.py

rem /*********** trying to install pyyaml with pip with ver specific  **********/
C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\song-play-schema-env\python -m pip install pyyaml==6.0

rem /*********** using python from the env folder  **********/
C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\song-play-schema-env\python

rem /*********** run create tables  **********/
C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\song-play-schema-env\python C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\create_tables.py
python create_tables.py

rem /*********** run etl  **********/
C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\song-play-schema-env\python C:\Users\josep\OneDrive\Documentos\projects\UdacityDeng\UDENG_L02P01\etl.py
python etl.py

