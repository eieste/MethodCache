####
Hack
####


You can simply write your own decorator, or imlement in your code
just simply call :code:`add_to_cache`

.. code-block:: python

    from methodcache.cache import add_to_cache
    main_store = Store(ttl=5)

    def dothings(a,b,c):
        time.sleep(5)
        return a+b+c


    add_to_cache(options={}, store=main_store, func=dothings, WrapperParameters((1,2,3)))


This is useful for the following Example

.. code-block:: python

    from methodcache.cache import add_to_cache
    from methodcache import Store

    # ToDo Write a Example