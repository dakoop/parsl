.. _configuration_section:

Configuration
=============

Parsl workflows are developed completely independently from their execution environment. Parsl offers an extensible configuration model through which the execution environment and communication with that environment is configured. Parsl is configured using :class:`~parsl.config.Config` object. For more information, see the :class:`~parsl.config.Config` class documentation. The following shows how the configuration can be loaded.

   .. code-block:: python

      import parsl
      from parsl.config import Config
      from parsl.executors.threads import ThreadPoolExecutor

      config = Config(
          executors=[ThreadPoolExecutor()],
          lazy_errors=True
      )
      parsl.load(config)

.. contents:: Example Site Configurations

.. note::
   Please note that all configuration examples below import a `user_opts` file where all user specific
   options are defined. To use the configuration, these options **must** be defined either by creating
   a user_opts file, or explicitly edit the configuration with user specific information.

Comet (SDSC)
------------

.. image:: https://ucsdnews.ucsd.edu/news_uploads/comet-logo.jpg

The following snippet shows an example configuration for executing remotely on San Diego Supercomputer Center's **Comet** supercomputer. The example uses an `SSHChannel` to connect remotely to Comet, the `SlurmProvider` to interface with the Slurm scheduler used by Comet and the `SrunLauncher` to launch workers.

.. literalinclude:: ../../parsl/tests/configs/comet_ipp_multinode.py


Cori (NERSC)
------------

.. image:: https://6lli539m39y3hpkelqsm3c2fg-wpengine.netdna-ssl.com/wp-content/uploads/2017/08/Cori-NERSC.png

The following snippet shows an example configuration for accessing NERSC's **Cori** supercomputer. This example uses the IPythonParallel executor and connects to Cori's Slurm scheduler. It uses a remote SSH channel that allows the IPythonParallel controller to be hosted on the script's submission machine (e.g., a PC).  It is configured to request 2 nodes configured with 1 TaskBlock per node. Finally it includes override information to request a particular node type (Haswell) and to configure a specific Python environment on the worker nodes using Anaconda.

.. literalinclude:: ../../parsl/tests/configs/cori_ipp_multinode.py


Theta (ALCF)
------------

.. image:: https://www.alcf.anl.gov/files/ALCF-Theta_111016-1000px.jpg

The following snippet shows an example configuration for executing on Argonne Leadership Computing Facility's **Theta** supercomputer.
This example uses the `IPythonParallel` executor and connects to Theta's Cobalt scheduler using the `CobaltProvider`. This configuration
assumes that the script is being executed on the login nodes of Theta.

.. literalinclude:: ../../parsl/tests/configs/theta_local_ipp_multinode.py


Cooley (ALCF)
------------

.. image:: https://today.anl.gov/wp-content/uploads/sites/44/2015/06/Cray-Cooley.jpg

The following snippet shows an example configuration for executing remotely on Argonne Leadership Computing Facility's **Cooley** analysis and visualization system.
The example uses an `SSHInteractiveLoginChannel` to connect remotely to Cooley using ALCF's 2FA token.
The configuration uses the `CobaltProvider` to interface with Cooley's scheduler.

.. literalinclude:: ../../parsl/tests/configs/cooley_ssh_il_single_node.py

Swan (Cray)
-----------

.. image:: https://www.cray.com/blog/wp-content/uploads/2016/11/XC50-feat-blog.jpg

The following snippet shows an example configuration for executing remotely on Swan, an XC50 machine hosted by the Cray Partner Network.
The example uses an `SSHChannel` to connect remotely Swan, uses the `TorqueProvider` to interface with the scheduler and the `AprunLauncher`
to launch workers on the machine

.. literalinclude:: ../../parsl/tests/configs/swan_ipp_multinode.py


CC-IN2P3
--------

.. image:: https://cc.in2p3.fr/wp-content/uploads/2017/03/bandeau_accueil.jpg

The snippet below shows an example configuration for executing from a login node on IN2P3's Computing Centre.
The configuration uses the `LocalProvider` to run on a login node primarily to avoid GSISSH, which Parsl does not support yet.
This system uses Grid Engine which Parsl interfaces with using the `GridEngineProvider`.

.. literalinclude:: ../../parsl/tests/configs/cc_in2p3_local_single_node.py

Midway (RCC, UChicago)
----------------------

.. image:: https://rcc.uchicago.edu/sites/rcc.uchicago.edu/files/styles/slideshow-image/public/uploads/images/slideshows/20140430_RCC_8978.jpg?itok=BmRuJ-wq

This Midway cluster is a campus cluster hosted by the Research Computing Center at the University of Chicago.
The snippet below shows an example configuration for executing remotely on Midway.
The configuration uses the `SSHProvider` to connect remotely to Midway, uses the `SlurmProvider` to interface
with the scheduler, and uses the `SrunProvider` to launch workers.

.. literalinclude:: ../../parsl/tests/configs/midway_ipp_multinode.py


Open Science Grid
-----------------

.. image:: https://hcc-docs.unl.edu/download/attachments/11635314/Screen%20Shot%202013-03-19%20at%202.19.28%20PM.png?version=1&modificationDate=1492720049000&api=v2

The Open Science Grid (OSG) is a national, distributed computing Grid spanning over 100 individual sites to provide tens of thousands of CPU cores.
The snippet below shows an example configuration for executing remotely on OSG.
The configuration uses the `SSHProvider` to connect remotely to OSG, uses the `CondorProvider` to interface
with the scheduler.

.. literalinclude:: ../../parsl/tests/configs/osg_ipp_multinode.py

Amazon Web Services
-------------------

.. image:: ./aws_image.png

.. note::
   Please note that `boto3` library is a requirement to use AWS with Parsl.
   This can be installed via `python3 -m pip install libsubmit+aws`

Amazon Web services is a commercial cloud service which allows you to rent a range of computers and other computing services.
The snippet below shows an example configuration for provisioning nodes from the Elastic Compute Cloud (EC2) service.
The first run would configure a Virtual Private Cloud and other networking and security infrastructure that will be
re-used in subsequent runs. The configuration uses the `AWSProvider` to connect to AWS

.. literalinclude:: ../../parsl/tests/configs/ec2_single_node.py


Further help
------------

For help constructing a configuration, you can click on class names such as :class:`~parsl.config.Config` or :class:`~parsl.executors.ipp.IPyParallelExecutor` to see the associated class documentation. The same documentation can be accessed interactively at the python command line via, for example::

    >>> from parsl.config import Config
    >>> help(Config)

