#!/bin/sh

coverage erase

coverage-2.7 run --source foalorm.orm.dbapiprovider,foalorm.orm.dbschema,foalorm.orm.decompiling,foalorm.orm.core,foalorm.orm.sqlbuilding,foalorm.orm.sqltranslation --branch -m unittest discover

coverage-3.4 run --source foalorm.orm.dbapiprovider,foalorm.orm.dbschema,foalorm.orm.decompiling,foalorm.orm.core,foalorm.orm.sqlbuilding,foalorm.orm.sqltranslation --branch -m unittest discover


coverage-2.7 run -a --source foalorm.orm.dbapiprovider,foalorm.orm.dbschema,foalorm.orm.decompiling,foalorm.orm.core,foalorm.orm.sqlbuilding,foalorm.orm.sqltranslation --branch sql_tests.py

coverage-3.4 run -a --source foalorm.orm.dbapiprovider,foalorm.orm.dbschema,foalorm.orm.decompiling,foalorm.orm.core,foalorm.orm.sqlbuilding,foalorm.orm.sqltranslation --branch sql_tests.py

coverage html
