##########
How to use
##########

****
TLDR
****

Just simple put @cache :code:`@cache` over your method.

Example:

.. code-block:: python

    from methodcache import cache

    @cache
    def dothings(*args, **kwargs):
        pass

******
@cache
******

Is the caching decorator.
use this decorator on methods you want to cache with the following optional kwargs:
  * store
  * category
  * ttl

=====
store
=====
For Attributes and thier documentaiton see :class:`methodcache.cache.cache`

:code:`@cache` can used without any parameters.

If the kwarg ``store`` is missing, it creates a default Store.
This default Store are safed as static attribute named :code:`_default_store` in the class
:class:`methodcache.store.Store`



==========
category
==========


If the kwarg ``category`` not set, a category named :code:`default` was used


Categories can be seperated in "groups". You can define in which group the current method is cached.
The groups can be interleaved via :code:`:`.
eg. :code:`car:manufacturer:model`

**Demo**


.. code-block:: python

    from methodcache import cache

    @cache(category="car:manufacturer")
    def get_manufacturer(*args, **kwargs):
        return ["BMW", "Opel", "VW", "Honda"]

    @cache(category="car:manufacturer:model")
    def get_model(manufacturer):
        models = {
            "BMW": ["CarType1", "CarType2", "CarType3"]
            "Opel": ["CarType4", "CarType5", "CarType6"]
        }
        return models[manufacturer]

    manufacturer = get_manufacturer()
    get_model(manufacturer[0])


If these example code was executed the Store objects the informations like:

.. code-block:: json

    {
        "car": {
            "manufacturer": {
                "method_store":{
                    "get_manufacturer": ["BMW", "Opel", "VW", "Honda"]
                },
                "model": {
                    "method_store": {
                        "get_model;BMW": ["CarType1", "CarType2", "CarType3"]
                    }
                }
            }

        }
    }

===
ttl
===

If the kwarg ``ttl`` is not set a default ttl of 5 minutes are set.

You can define a TTL by createing a Store object.
This TTL from Store can be overwriten by :code:`@cache`

TTLs are always in Seconds

.. code-block:: python

    # TTL of 5 Minutes
    @cache(ttl=60*5)

The code Above is strongly simplified. In orginal software the arguments are also check.

*****
Store
*****

The Store object contains all caching information.

By initializeation you can set a default ttl.

.. code-block:: python

    st = Store(ttl=60*5)


to use the store as cache in for an app define it as handover parameters :code:`store`

.. code-block:: python

    st = Store(ttl=60*5)

    @cache(store=st)
    def dothings()
        pass

You can define multiple Stores to seperate your Application section from each other

************
Full Example
************

.. literalinclude:: ../../../example.py
   :language: python
