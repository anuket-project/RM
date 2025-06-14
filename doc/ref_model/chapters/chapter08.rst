Hybrid Multicloud: Data Centre to Edge
======================================

Introduction to Hybrid Multicloud
---------------------------------

The :ref:`chapters/chapter03:modelling` section focuses on cloud infrastructure abstractions. While these are generic
abstractions, they and the associated capabilities of the cloud infrastructure are specified for data centres, central
offices, and colocation centres. The environmental conditions, facility and other constraints, and the variability of
deployments on the edge are significantly different and therefore require separate consideration.

It is unrealistic to expect a private cloud to meet the needs of all the workloads in a cost-effective way when the
private cloud must also meet the needs for peak loads and disaster recovery. For this reason alone, enterprises will
need to implement a hybrid cloud. In a hybrid cloud deployment, two or more distinct cloud infrastructures are
interconnected. In a multicloud, the distinct cloud infrastructures of the hybrid cloud may be implemented using one
or more technologies. The hybrid multicloud infrastructure has differences requiring different abstractions. These
hybrid multiclouds can be considered to be federated.

In the :ref:`chapters/chapter03:modelling` section, the cloud infrastructure is defined. The tenants are required to
provide certain necessary services, such as load balancer (LB) and messaging. Therefore, the VNF/CNFs incorporate
different versions of the same services with the resultant issues related to an explosion of services, together with
their integration and management complexities. To mitigate these issues, the Reference Model must specify the common
services that every Telco cloud must support, and thereby require workload developers to utilise these prespecified
services.

A generic Telco cloud is a hybrid multicloud, or a federated cloud, that has deployments in large data centres,
central offices or colocation facilities, and the edge sites. This chapter discusses the characteristics of Telco
edge and hybrid multicloud.

Hybrid multicloud architecture
------------------------------

The GSMA white paper "Operator Platform Concept Phase 1: Edge Cloud Computing" (January 2020) states: "Given the wide
diversity of use cases that the operators will tasked to address, from healthcare to industrial IoT, it seems logical
for operators to create a generic platform that can package the existing assets and capabilities (e.g., voice messaging,
IP data services, billing, security, identity management, etc. ...) as well as the new ones that 5G makes available
(e.g., Edge cloud, network slicing, etc.) in such a way as to create the necessary flexibility required by this new
breed of enterprise customers."

Cloud computing has evolved and matured since 2010 when NIST :cite:p:`NIST-SP-800-145` published its definition of cloud computing,
with its 5 essential characteristics, 3 service models and 4 deployment models.

The generic model for an enterprise cloud has to be "hybrid", with the special cases of purely private or public clouds
as subsets of the generic hybrid cloud deployment model. In a hybrid cloud deployment, two or more distinct cloud
infrastructures are interconnected.

Cloud deployments can be created using a variety of technologies, such as OpenStack and Kubernetes, and commercial
technologies, such as VMware, AWS, Azure, and so on. A multicloud deployment can use more than one technology at a time.

A generic Telco cloud is a hybrid multicloud. However, a better way to describe it would be a federation of clouds, or
a federated cloud. The principal charactreristics of a federated cloud are as follows:

- A federated cloud is a collection of cooperating, interoperable autonomous component clouds.
- The component clouds perform their local operations (internal requests), while at the same time participating in the
  federation and responding to other component clouds (external requests).

  - the component clouds are autonomous in terms of, for example, execution autonomy; please note that in a centralised
    control plane scenario (please see the section "Centralised Control Plane" in the
    "Edge Computing: Next Steps in Architecture, Design and Testing" whitepaper :cite:p:`openinfraedgearch`) the edge clouds do not have
    total autonomy and are subject to constraints (e.g., workload LCM)
  - execution autonomy is the ability of a component cloud to decide the order in which internal and external requests
    are performed
  - also, a federation controller does not impose changes to the component cloud except for running some central
    component(s) of the federated system (for example, a broker agent – executes as a workload)

- The component clouds are likely to differ in, for example, infrastructure resources and their cloud platform software.
- Workloads may be distributed on single or multiple clouds, where the clouds may be co-located or geographically
  distributed.
- The component clouds only expose their northbound APIs (NBIs). Note that VMware deployed in a private and a public
  cloud can be treated as a single cloud instance.

Characteristics of a federated cloud
------------------------------------

In this section, we will further explore the characteristics of the federated cloud architecture and the architecture
building blocks that constitute the federated cloud. For example, :numref:`Example hybrid multicloud component cloud`
shows a Telco cloud that consists of four sub-clouds:

- Private on premise
- Cloud vendor provided on premise
- Private outsourced (commercial cloud provider, such as a Hyperscaler Cloud Provider (HCP)
- Public outsourced (see the diagram below)

Such an implementation of a Telco cloud allows for a mix and match of price points, flexibility in market
positioning and time to market, capacity with the objective of attaining near unlimited capacity, scaling within a
sub-cloud or through bursting across sub-clouds, access to local capacity near the user base, and access to
specialised services.

.. figure:: ../figures/RM-Ch08-HMC-Image-1.png
   :name: Example hybrid multicloud component cloud
   :alt: Example hybrid multicloud component cloud

   Example hybrid multicloud component cloud

Telco cloud
-----------

The :numref:`Telco Cloud: Data Centre to Edge` presents a visualisation of a Telco operator cloud, or Telco cloud,
with clouds and cloud components distributed across regional data centres, metro locations, such as a central
office or a co-location site, and at the Edge, that are interconnected using a partial mesh network. Note that at
the regional centre level the interconnections are likely to form a denser mesh, while at the edges they are likely
to form a sparser mesh.

.. figure:: ../figures/RM-Ch08-Multi-Cloud-DC-Edge.png
   :name: Telco cloud: data centre to edge
   :alt: Telco Cloud: data centre to edge

   Telco cloud: data centre to edge

The Telco operator may own and/or have partnerships and network connections to utilize multiple clouds for network
services, IT workloads, and external subscribers. The types of the component clouds include the following:

- On-Premise Private

  - On-Premise Private is open-source, deployed and managed by the operator or the vendor, and based on OpenStack
    or Kubernetes.
  - On-Premise Private is developed by the vendor and is deployed and managed by the operator or the vendor.
    Examples: Azure on Prem, VMware, Packet, Nokia, Ericsson, and so on.

- On-Premise Public: This commercial cloud service is hosted at the operator location, but is intended for
  operator and public use. Example: AWS Wavelength.
- Outsourced Private: With this component cloud, hosting is outsourced. Hosting can be at a commercial cloud
  service. Examples: Equinix, AWS, and so on.
- (Outsourced) Public: This is a commercial cloud service. Examples: AWS, Azure, VMware, and so on.
- Multiple different clouds can be co-located in the same physical location and may share some of the physical
  infrastructure (for example, racks).
- Outsourced Private: hosting outsourced. Hosting can be at a commercial cloud service. Examples: Equinix,
  AWS, and so on.
- (Outsourced) Public: This is a commercial cloud service. Examples: AWS, Azure, VMware, and so on.
- Multiple different clouds can be co-located in the same physical location and may share some of the physical
  infrastructure (for example, racks).

In general, a Telco cloud consists of multiple interconnected large data centres that serve transcontinental
areas or regions. A Telco cloud region may connect to multiple regions of another Telco cloud via large-capacity
networks. A Telco cloud also consists of interconnected local/metro sites (multiple possible scenarios). A local
site cloud may connect to multiple regions within that Telco cloud or in another Telco cloud. A Telco cloud also
consists of a large number of interconnected edge nodes. These edge nodes may be impermanent. A Telco cloud's
edge node may connect to multiple local sites within that Telco cloud or in another Telco cloud. An edge node
may rarely connect to a Telco cloud region.

Table 8-1 provides the essential information about the types of deployments, and responsible parties for cloud
artefacts.

+------------------+-------------------+--------------------+-----------------+------------------+---------------------+
| Type             | System developer  | System maintenance | System operator | Location where   | Primary resource    |
|                  |                   |                    | and manager     | deployed         | consumption models  |
+==================+===================+====================+=================+==================+=====================+
| Private          | Open-source       | Self/vendor        | Self/vendor     | On-premise       | Reserved, dedicated |
| (internal users) |                   |                    |                 |                  |                     |
+------------------+-------------------+--------------------+-----------------+------------------+---------------------+
| Private          | Vendor, HCP       | Self/vendor        | Self/vendor     | On-premise       | Reserved, dedicated |
+------------------+-------------------+--------------------+-----------------+------------------+---------------------+
| Public           | Vendor, HCP       | Self/vendor        | Self/vendor     | On-premise       | Reserved, on-demand |
+------------------+-------------------+--------------------+-----------------+------------------+---------------------+
| Private          | HCP               | Vendor             | Vendor          | Vendor locations | Reserved, dedicated |
+------------------+-------------------+--------------------+-----------------+------------------+---------------------+
| Public           | HCP               | Vendor             | Vendor          | Vendor locations | On-demand, reserved |
| (all users)      |                   |                    |                 |                  |                     |
+------------------+-------------------+--------------------+-----------------+------------------+---------------------+

**Table 8-1:** Cloud types and the parties responsible for the artefacts

Telco operator platform conceptual architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`Conceptual Architecture of a Telco Operator Platform` shows a conceptual Telco operator platform architecture.
The cloud infrastructure resources layer exposes virtualised (including containerised) resources on the physical
infrastructure resources and also consists of various types of virtualisation and management software (see details
later in this chapter). The cloud platform components layer makes available both elementary and composite objects for
use by application and service developers, and for use by services during runtime. The cloud services layer exposes the
services and applications that are available to the users. Some of the services and applications may be sourced from or
executed on other cloud platforms. Note that while the architecture is shown as a set of layers, this is not an
isolation mechanism. Therefore, users may, for example, access the cloud infrastructure resources directly without
interacting with a broker.

.. figure:: ../figures/RM-Ch08-Telco-Operator-Platform.png
   :name: Conceptual architecture of a Telco operator platform
   :alt: Conceptual architecture of a Telco operator platform

   Conceptual architecture of a Telco operator platform

The cloud services and the cloud resources brokers provide value-added services in addition to the fundamental
capabilities such as service and resource discovery. These brokers are critical for a multicloud environment to
function and utilise cloud-specific plugins to perform the necessary activities. These brokers can, for example,
provision and manage environments with resources and services for machine learning (ML) services, augmented/virtual
reality, or specific industries.

Multicloud interactions model
-----------------------------

To realise a federated cloud requires the definition of, and agreement on, a set of APIs. These APIs should allow
each of the parties to interact cooperatively. They need to cover the management layer: business management and
service operations interactions, as well as the data plane, customer and user, transactions, and conversational
interfaces.

As outlined in :numref:`Conceptual Architecture of a Telco Operator Platform` above, the exposure point for the
management interactions is the Cloud Service Broker and the Cloud Resource Broker. The set of interactions that
these interface points need to provide are defined by the :numref:`Multicloud interactions model` below.
:numref:`Multicloud interactions model` provides a taxonomy for the interactions between the communications
service provider and the cloud providers.

.. figure:: ../figures/rm-chap-8-multicloud-interactions-03.png
   :name: Multicloud interactions model
   :alt: Multicloud interactions model

   Multicloud interactions model

The multicloud interactions model defines the following core roles:

- Communications service provider (CSP): this is the party responsible for providing an end-user service to the
  customer.
- Customer/user: these are the parties that use the service (user), and establish the business agreement for the
  service provision (customer). For retail services, the customer and the user are the same party, while for
  enterprise services, the enterprise is the customer (responsible for the business agreement), and its
  representatives are the users.
- Cloud providers: these are the parties that provide the cloud services. These services could be any XaaS
  service. A CSP may have an agreement with a SaaS cloud, which in turn uses an IaaS cloud provider to deliver
  their service.

The set of high-level interactions covers the following:

- Manage account and catalog: this covers the account, users, subscriptions, billing, and the catalogue of
  the available services, where the service provider (not necessarily CSP-only) is responsible for the creation
  and publication of the catalogue contents.
- Manage connectivity: this covers the public or private network, the VPN configuration, the CSP edge/cloud
  Connection configuration, and the Connection Security Profile.
- Manage resource: this covers resource pool management, VM/VNF management (CPU, memory, storage, and network),
  image repository management, storage management, VNF/CNF LCM, and monitoring of resources.
- Manage app/VNF: this covers image/container/registry management, deploy/configure/scale/start/stop app/VNF,
  and monitoring of app/VNFs.
- Transactions/conversations: this convers the Use Communications Services, Use Edge Applications Services,
  and Use Cloud Services.

This model, its actors (roles), and the interactions discussed below, are focused on the provision and 
consumption of the cloud services in different stereotypical deployment scenarios: IaaS, SaaS, CaaS, and Edge.
The model presented in Chapter 9 deals with the cloud build and maintenance processes in different scenarios.
It also defines the boundaries of the automation domains. These two views complement each other.

Stereotypical scenarios
~~~~~~~~~~~~~~~~~~~~~~~

A set of stereotypical interactions cases are illustrated for simple Infrastructure-as-a-Service (IaaS) and
Software-as-a-Service (SaaS) cases, where deployment is on a cloud provider's centralised sites and/or edge
sites. The scenarios help to highlight the needs for the cloud service broker and the cloud resources broker
(in accordance with :numref:`Conceptual Architecture of a Telco Operator Platform`), and therefore the extent
of the orchestration required to manage the interactions.

.. figure:: ../figures/rm-chap8-multi-cloud-interactions-simple-stereo-types-03.png
   :name: Simple stereotypical interactions
   :alt: Simple stereotypical interactions

   Simple stereotypical interactions

The following patterns are visible:

- For IaaS cloud integration:

  - The cloud behaves like a set of virtual servers. Therefore, it requires virtual server lifecycle management
    and orchestration.
  - Depending on whether the cloud is accessed via the public internet or a private connection changes the
    extent of the connectivity management.

- For SaaS cloud integration:

  - The cloud behaves like a running application/service. It requires subscription management. Complex
    orchestration of the app/service and underlying resources is managed by the SaaS provider. The user is
    relieved of having to provide direct control of the resources.

- For CaaS cloud integration:

  - The registry for pulling the containers could be from either of the following:

    - The cloud. In this case, the consumption model is closer to SaaS.
    - A private or public registry. In this case, the integration model requires specific registry
      management elements.

- For edge cloud integration:

  - This scenario adds the requirement for the communications service provider and the cloud provider
    to provide physical, network underlay and overlay connectivity management.

A disaggregated scenario for a CSP using SaaS that uses IaaS is illustrated in the following diagram:

.. figure:: ../figures/rm-chap8-multi-cloud-interactions-disaggregated-stereo-type-02.png
   :name: Disaggregated SaaS stereotypical interaction
   :alt: Disaggregated SaaS stereotypical interaction

   Disaggregated SaaS stereotypical interaction

In the disaggregated SaaS scenario, the application provider can operate as an "infra-structureless"
organisation. This may be achieved through SaaS organisation using public IaaS Cloud Providers, which
could include the CSP itself. A key consideration for CSP in both cloud provision and consumption in
multicloud scenarios is how to manage the integration across the cloud providers.

To make this manageable and to avoid integration complexity, there are a number of models. They are as
follows:

- Industry-standard APIs that allow consistent consumption across cloud providers.
- API brokerage, which provides a consistent set of consumer-facing APIs that manage adaption to
  proprietary APIs.
- Cloud brokerage, where the brokerage function is provided as a service and allows a "single pane of
  glass" to be presented for the management of the multicloud environment.

The different means of integrating with and managing cloud providers is broadly covered under the
umbrella topic of cloud management platforms. A survey of applicable standards for achieving this is
provided in section 8.5.2. Requirements, reference architecture and industry standards intersect.

The API and cloud brokerage models are illustrated in the following diagrams:

.. figure:: ../figures/rm-chap8-multi-cloud-interactions-api-brokerage-stereo-type-02.png
   :name: API brokerage multicloud stereotypical interaction
   :alt: API brokerage multicloud stereotypical interaction

   API brokerage multicloud stereotypical interaction

.. figure:: ../figures/rm-chap8-multi-cloud-interactions-cloud-brokerage-stereo-type-02.png
   :name: Cloud brokerage multicloud stereotypical interaction
   :alt: Cloud brokerage multicloud stereotypical interaction

   Cloud brokerage multicloud stereotypical interaction

.. _requirements-reference-architecture--industry-standards-intersect:

Requirements, reference architecture and industry standards intersect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The communications service provider (CSP) is both a provider and a consumer of cloud-based services.
When the CSP is acting as a consumer, then the typical consideration is the total cost of ownership,
as the consumption is usually to support internal business operations and BSS/OSS systems.
When the CSP is acting as a provider of cloud services, through the operation of their own cloud or
the reselling of the cloud services, then the typical consideration is marginal (cost to offer
services versus income received).

These two stances will drive differing approaches to how a CSP would look, in order to manage the
way it interacts within a multicloud environment.

As a consumer of cloud services to support internal business operations and BSS/OSS, the focus is on meeting the needs
of the organisation's applications . Historically, this came with the need to operate and support the organisation's
infrastructure needs. This resulted in the splitting of the CIO organisation into Delivery and Operations groups. At
the same time that the CIO application workloads are moving to SaaS and other cloud providers, the CTO network systems
are migrating from running on custom-dedicated infrastructure to run on virtualised COTS infrastructure. Examples of
this include IMS and 3GPP (4G and 5G) functions. IP routers and firewalls are being provided as VNFs and CNFs. These
network workloads are now also being deployed in private CSP clouds, as well as in public clouds.

As outlined in section "8.4 Telco Cloud", the result is that the CSP network is now an interconnected set of
distributed cloud infrastructures supported by different cloud providers, including the CSP. Therefore, the term
Hybrid Multicloud, and the need for the CSP to be able to support and use this interconnected cloud, are both
inevitable and essential.

As a consumer and provider of cloud services, the necessity for the CSP to build and manage its own cloud
infrastructure will continue. The CSP will also have to provide the following:

- Cloud orchestration solutions, to orchestrate the use of cloud services and capabilities from its own and other
  cloud providers.
- Network orchestration solutions, to manage the interconnectivity across its own and other cloud provider networks.

The interactions for this are outlined in the Multicloud Interactions Model. However, to realise this, the CSP
will need to adopt and sponsor a set of standards that are necessary to support these interactions. The
identification of existing applicable standards and gaps across the interactions needs to be completed. As a first
step, the following criteria for the inclusion of a standard/technology is defined. The following must be true of
these standards and technologies:

- They must provide the capabilities that are necessary to achieve a hybrid multicloud vision and multicloud
  interactions.
- They must be already mature Open Standards that have either been adopted or nurtured by recognised bodies with
  the telecommunications industry (for example, ITU, ETSI, TMForum, GSMA, 3GPP, ISO, and national standards
  organisations, such as ANSI, NIST, and so on).
- They must have reference implementations, or active open source projects or consortia providing implementations
  (for example, the Cloud Native Computing Foundation (CNCF) and the Open Infrastructure Foundation).
- They must allow the CSP to source delivery and support services based on these from multiple vendors.
- They must allow the CSP to actively contribute to and request the capabilities and coverage of the standard or
  technology.
- They must not be the sole property of a vendor or company.
- They must not be focused on transactions or conversations, or user or data plane standards (typically IETF, IEEE,
  MEF/Carrier Ethernet, and so on).

Hybrid, Edge, and Multicloud unified management Platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As organisations spread their resources across on-premises, multiple clouds, and the edge, there is a clear need
for a single set of tools and processes to manage and operate across these hybrid, edge, and multiclouds (HEM
clouds), as can be seen from the following simplified scenarios.

Scenario: An operator has private clouds that they use for their workloads. Over time, the operator evolves the
environment of these private clouds:

- A: The operator has decided to use one or more public clouds for some of their workloads.
- B: The operator has decided to use an edge cloud for some of their clients.
- C: The operator has decided to create edge clouds for some of their clients.

Scenario B can be treated as the same as Scenario A. Scenario C is akin to the private cloud, except for the location
and control over the facilities at that location. For its workloads, the operator will have to use the target clouds
tools or APIs to create the necessary accounts, billing arrangements, quotas, and so on. The operator then creates the
necessary resources, such as VMs or Kubernetes clusters, and so on. The operator follows up with creating needed
storage, networking, and so on, before onboarding the workload and operating it. This is a complex task, even when the
operator is dealing with only one other cloud, in addition to operating their own cloud. The operator is faced with
a number of challenges, including acquiring a new set of skills, knowledge of APIs, tools, and the complexity of
managing different policies, updates, and so on. This becomes impossible to manage when incorporating more than one
other cloud. Hence the need for a single pane of glass.

This Hybrid, Edge, and Multicloud unified management Platform (HEMP), also known as single pane of glass, provides
the capabilities to consistently perform the following set of tasks through a common set of governance and
operational practices:

- Manage accounts, credentials, resources, and services across facilities (regions, data centres, and edge
  locations).
- Interoperate the different clouds.
- Implement common policies and governance standards.
- Manage a common security posture.
- Provide an integrated visualisation into the infrastructure and workloads.

GSMA's Operator Platform Group (OPG) specifies a federated model and the requirements for the edge platforms
(Operator Platform Telco Edge Requirements v2.0 :cite:p:`gsmaopg02`)  While the document is for edge, most of the
requirements can be applied to other cloud deployments. Anuket RM is implementation agnostic, that is, whether
the implementation uses agents, federations, or other mechanisms.

The following tables list some of the requirements for the Hybrid, Edge, and Multicloud operator Platform (HEMP).
These requirements are in addition to the requirements in other chapters of this RM.

**HEMP general requirements**

.. list-table:: General requirements of the Hybrid, Edge, and Multicloud operator Platform (HEMP)
   :widths: 10 20 20
   :header-rows: 1

   * - Ref
     - Requirement
     - Definition/Note 
   * - hem.gen.001
     - The HEMP should only use published APIs in managing component clouds.
     - For example, to accomplish the example in `hem.gen.003`, it uses the published APIs of the target cloud.
   * - hem.gen.002
     - The HEMP should publish all of the APIs used by any of its components.
     - For example, the available GUI portal only uses APIs that have been published by the HEMP.
   * - hem.gen.003
     - The HEMP should provide common terms for interaction with its constituent clouds.
     - For example, “create Account” should be used across the different clouds.
   * - hem.gen.004
     - The HEMP should generalise and define a common set of resources available to be managed in the constituent
       clouds.
     - Example resources include hosts (including BareMetal), virtual machines (VMs), vCPU, memory, storage, network,
       kubernetes clusters, kubernetes nodes, images (OS and others), and credentials. For the private cloud, additional
       example resources include racks, ToR/CE switches, and platform images.
   * - hem.gen.005
     - The HEMP should provide a common interface for managing component clouds.
     - 
   * - hem.gen.006
     - The HEMP should expose resources from all the cloud operators and locations (regions, sites, and so on).
     - See the example resources in `hem.gen.004`
   * - hem.gen.007
     - The HEMP should allow reservation of resources, if the component cloud operator allows it.
     - 
   * - hem.gen.008
     - The HEMP should support multitenancy.
     - 

**Table 8-2:** General requirements of the Hybrid, Edge, and Multicloud operator Platform (HEMP)

**Requirements of HEMP operations**

+-------------+--------------------------------------------------------+-----------------------------------------------+
| Ref         | Requirement                                            | Definition/Note                               |
+=============+========================================================+===============================================+
| hem.ops.001 | The HEMP should generalise and define a common set of  |                                               |
|             | management operations available in the constituent     |                                               |
|             | clouds. Required operations include: create, deploy,   |                                               |
|             | configure, start, suspend, stop, resume, reboot,       |                                               |
|             | delete, scale, and list. Some operations may only be   |                                               |
|             | available for a subset of resources.                   |                                               |
+-------------+--------------------------------------------------------+-----------------------------------------------+
| hem.ops.002 | The HEMP should centrally manage all resources (across |                                               |
|             | all constituent clouds).                               |                                               |
+-------------+--------------------------------------------------------+-----------------------------------------------+
| hem.ops.003 | The HEMP should centrally operate all constituent      |                                               |
|             | clouds.                                                |                                               |
+-------------+--------------------------------------------------------+-----------------------------------------------+
| hem.ops.004 | The HEMP should provide mechanisms to integrate new    | This may require pre-development of necessary |
|             | clouds.                                                | capabilities for the support of HEMP          |
|             |                                                        | abstractions, and impementation of            |
|             |                                                        | connectivity with the new cloud               |
+-------------+--------------------------------------------------------+-----------------------------------------------+
| hem.ops.005 | The HEMP should provide mechanisms to drop a           | For example, the provided GUI portal shall    |
|             | constituent cloud.                                     | only use HEMP published APIs                  |
+-------------+--------------------------------------------------------+-----------------------------------------------+
| hem.ops.006 | The HEMP should provide mechanisms and processes for   |                                               |
|             | onboarding existing assets (such as resources,         |                                               |
|             | connectivity, and so on).                              |                                               |
+-------------+--------------------------------------------------------+-----------------------------------------------+
| hem.ops.007 | The HEMP should provide mechanisms and processes for   |                                               |
|             | the automated configuration management of all          |                                               |
|             | environments and resources.                            |                                               |
+-------------+--------------------------------------------------------+-----------------------------------------------+

**Table 8-3:** Operability requirements of the Hybrid, Edge, and Multicloud operator Platform (HEMP)

**HEMP LCM requirements**

+-------------+--------------------------------------------------------+-----------------------------------------------+
| Ref         | Requirement                                            | Definition/Note                               |
+=============+========================================================+===============================================+
| hem.lcm.001 | The HEMP should monitor all environments and assets.   |                                               |
+-------------+--------------------------------------------------------+-----------------------------------------------+
| hem.lcm.002 | The HEMP should provide visibility into the health of  |                                               |
|             | all assets.                                            |                                               |
+-------------+--------------------------------------------------------+-----------------------------------------------+
| hem.lcm.003 | The HEMP should provide capabilities for centralised   |                                               |
|             | visibility and management of all alerts.               |                                               |
+-------------+--------------------------------------------------------+-----------------------------------------------+
| hem.lcm.004 | The HEMP should provide capabilities for the           | This does not preclude local log analytics.   |
|             | centralised analysis of all logs.                      |                                               |
+-------------+--------------------------------------------------------+-----------------------------------------------+

**Table 8-4:** Lifecycle Management (LCM) requirements of the Hybrid, Edge, and Multicloud operator Platform (HEMP)

**HEMP security requirements**

.. list-table:: HEMP security requirements
   :widths: 20 60 20
   :header-rows: 1

   * - hem.sec.001
     - Requirement: The HEMP should provide capabilities for the centralised management of all security policies.
     - Definition/Note: (empty)
   * - hem.sec.002
     - Requirement: The HEMP should provide capabilities for the centralised tracking of compliance of all security requirements (:ref:`chapters/chapter07:consolidated security requirements`).
     - Definition/Note: (empty)
   * - hem.sec.003
     - Requirement: The HEMP should provide capabilities for insights into the changes that resulted from resource non-compliance.
     - Definition/Note: (empty)

**Table 8-5:**  Hybrid, Edge, and Multicloud operator Platform (HEMP) security requirements


Aspects of multicloud security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cloud infrastructures, emerging as a key element in the Telco operator ecosystem, are part of the attack surface
landscape. This is particularly worrying with the 5G rollout becoming a critical business necessity. It is important to
be vigilant regarding the cloud-focused threats and associated adversarial behaviours, methods, tools, and strategies
that cyber threat actors use. In the multicloud ecosystem, composed of different security postures and policies, network
domains, products, and business partnerships, the responsibility for managing the different cloud environments necessary
to support 5G use cases falls to different enterprises, creating new levels of complexities and a new range of security
risks.

For services deployed on hybrid multicloud environments, the security responsibility can be
delegated to cloud service providers. However, the Telco operator is always accountable for their
customers' data protection (at rest, in transit, and in use) and for the security posture of
the deployments. It implies that a consistent security posture is ensured across multiple
cloud service providers. The white paper "Evolving 5G security for the cloud", 5G Americas,
September 2022, addresses this issue. A Mobile Network Operator (MNO) deploying 5G networks
in a hybrid multicloud environment is a cloud consumer and is accountable for the security
of all the layers of the cloud stack. The white paper details the cloud shared security model
in the three cloud service models: IaaS, PaaS, and SaaS. The MNO must ensure the cloud
service agreement articulation of the security responsibilities. The white paper also
highlights the importance of applying a zero-trust mindset for cloud-based deployment,
for RAN and core functions to secure the networks.

In a hybrid multicloud environment, there are additional security principles that need to be considered.
These principles, set out in the table below, are drawn from the collaboration with the GSMA Fraud and
Security Group (FASG) and the "5G security Guide", FS.40 v2.0 document :cite:p:`gsmafs40`.

+--------------------------------+-------------------------------------------------------------------------------------+
| Multicloud security principle  | Description                                                                         |
+================================+=====================================================================================+
| Policy synchronization         | Consistency in applying the right security policies across environments, services,  |
|                                | interfaces, and configured resources.                                               |
+--------------------------------+-------------------------------------------------------------------------------------+
| Visibility                     | A common data model approach to share events and behaviours across all the key      |
|                                | compute, storage, network, and applications resources; environments, virtualised    |
|                                | platforms, containers, and interfaces.                                              |
+--------------------------------+-------------------------------------------------------------------------------------+
| Monitoring                     | Centralisation, correlation, and visualisation of security information across the   |
|                                | different cloud environments, to provide an end-to-end view and enable timely       |
|                                | response to attacks.                                                                |
+--------------------------------+-------------------------------------------------------------------------------------+
| Automation                     | Automation of critical activities, including cloud security posture management,     |
|                                | continuous security assessments, compliance monitoring, detection of                |
|                                | misconfigurations, and identification and remediation of risks.                     |
+--------------------------------+-------------------------------------------------------------------------------------+
| Access management              | A wide range of users, including administrators, testers, DevOps, and developers    |
|                                | and customers, should be organised into security groups with privileges appropriate |
|                                | to the different resources and environments.                                        |
+--------------------------------+-------------------------------------------------------------------------------------+
| Security operations model      | Augmentation of security services provided by cloud service providers, with the     |
|                                | vetted third-party and/or open-source tools and services, all incorporated into the |
|                                | established overall security operations model.                                      |
+--------------------------------+-------------------------------------------------------------------------------------+

**Table 8-6:**  Multicloud security principles

For Telco operators to run their network functions in a multicloud environment, specifically, in public clouds, the
industry will need a set of new standards and new security tools to manage and regulate the interactions between
the parties participating in the multicloud. For an example of a step in this direction, see ETSI specification
TS 103 457 :cite:p:`TS-103-457cyber` “Interface to offload sensitive functions to a trusted domain”. This document
provides extra security requirements for public clouds, to allow Telco operators the option of running network functions
in public clouds.

There is another security aspect to consider, which is related to the autonomous nature of the participants in the
multicloud. We can prescribe certain things and if not satisfied treat that party as "untrusted". This problem has been
addressed to some extent in TS 103 457. This standard introduces the idea of a Less Trusted Domain (LTD) and a More
Trusted Domain (MTD), and specifies the Trusted Cross-Domain Interface (TCDI) to standardise secure interactions
between them. The standard defines the following elementary functions of the TCDI:

- Connection and session management
- Data and value management
- Transferring cryptography functionality. This comprises the following:

 - Entropy request
 - Encryption keys request
 - Trusted timestamping
 - Secure archive
 - Secure storage
 - Search capabilities

As described in section 1 Scope of the TS 103 457 document :cite:p:`etsits103sp457`, it specifies "a high-level
service-oriented interface, as an application layer with a set of mandatory functions, to access secured services
provided by, and executed in a More Trusted Domain. The transport layer is out of scope and left to the architecture
implementation". The standard provides extra security features for sensitive functions, down to individual virtual 
machines or containers. As such, it is recommended that the relevant components of the reference models, reference
architecture, reference implementations, and reference compliance take note of this standard and ensure their
compatibility, wherever possible.

Telco Edge Cloud (TEC)
----------------------

This section presents the characteristics and capabilities of different edge cloud deployment locations,
infrastructure, footprint, and so on. Note that many terms are used in this section. For this reason, this section
includes a table that tries to map these different terms.

Telco Edge Cloud: deployment environment characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Telco Edge Cloud (TEC) deployment locations can be in any of the following environments:

- Friendly environments, such as offices, apartments, or other similar indoor locations.
- Challenging environments, such as busy streets, near to network radio transmitters, or other noisy outdoor locations.
- Harsh environments: places where there is a likelihood of chemical, heat, or electromagnetic exposure, such as
  factories, power stations, processing plants, and so on.

Some of the more salient characteristics can be seen in Table 8-7.

.. list-table:: TEC deployment location characteristics and capabilities
   :widths: 10 20 10 10 10 20 20
   :header-rows: 1

   * - Environmental type
     - Facility type
     - Environmental characteristics
     - Capabilities
     - Physical security
     - Implications
     - Deployment locations
   * - Environmentally friendly
     - Indoors: typically commercial or residential buildings.
     - Protected, and therefore safe for common infrastructure.
     - - Easy access to a continuous electricity supply.
       - High/medium bandwidth.
       - Fixed and/or wireless network access.
     - Controlled access
     - Commoditised infrastructure with minimal need or no need for hardening or ruggedisation. Operational benefits for
       installation and maintenance.
     - Indoor venues: homes, shops, offices, stationary and secure cabinets, data centres, central offices, colocation
       facilities, vendor premises, customer premises.
   * - Environmentally challenging
     - Outdoors and/or exposed to environmentally harsh conditions.
     - - Lack of protection.
       - Exposure to abnormally high levels of noise, vibration, heat, chemical, and electromagnetic pollution. 
     - - Possibility of devices having to rely on battery power only.
       - Low/medium bandwidth.
       - Fixed and/or mobile network access.
     - Little or no access control.
     - - Ruggedisation is likely to be expensive.
       - The system is likely to be complex to operate.
     - Example locations: curb side, near cellular radios.

**Table 8-7:** TEC deployment location characteristics and capabilities

Telco Edge Cloud: infrastructure characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Commodity hardware is only suited for environmentally friendly environments. Commodity hardware has standardised
designs and form factors. Cloud deployments in data centres typically use such commodity hardware with standardised
configurations. This results in operational benefits for procurement, installation, and ongoing operations.

In addition to the type of infrastructure hosted in the data centre clouds, facilities with smaller infrastructure
deployments, such as central offices or colocation facilities, may also host non-standard hardware designs, including
specialised components. The introduction of specialised hardware and custom configurations increases the cloud
operations and management complexity.

At the edge, the infrastructure may further include ruggedised hardware for harsh environments and hardware with
different form factors. With the evolution of the Internet of Things (IoT) and ubiquitous connectivity (including
personal devices) to consider extreme-edge devices as part of the ecosystem, this will require the infrastructure
to integrate with and offer programmability and processing capabilities for these devices. 

The end-to-end orchestration will need to support the extreme edge use cases.

Telco Edge Cloud: infrastructure profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :ref:`chapters/chapter04:profiles and workload flavours` section specifies the following two infrastructure
profiles:

- The **Basic** cloud infrastructure profile. This is intended for use by both IT and Network Function workloads that
  have low to medium network throughput requirements.
- The **High Performance** cloud infrastructure profile. This is intended for use by applications that have high network
  throughput requirements (up to 50 Gbps).

The High-Performance profile can specify extensions for hardware offloading. For details, see
:ref:`chapters/chapter03:hardware acceleration abstraction`. The Reference Model High-Performance profile
includes an initial set of :ref:`chapters/chapter04:profile extensions`.

Based on the infrastructure deployed at the edge, Table 8-8 specifies the
:ref:`chapters/chapter05:feature set and requirements from infrastructure` that would
need to be relaxed.

.. list-table:: TEC exceptions to infrastructure profile features and requirements
   :widths: 10 10 10 20 20 20 10
   :header-rows: 1

   * - Reference
     - Feature
     - Description
     - As specified in RM Chapter 05 - Basic type
     - As specified in RM Chapter 05 - High performance
     - Exception for edge - Basic type
     - Exception for edge - High performance
   * - infra.stg.cfg.003
     - Storage with replication
     - 
     - N
     - Y
     - N
     - Optional
   * - infra.stg.cfg.004
     - Storage with encryption
     - 
     - Y
     - Y
     - N
     - Optional
   * - infra.hw.cpu.cfg.001
     - Minimum number of CPU sockets
     - This determines the minimum number of CPU sockets within each host.
     - 2
     - 2
     - 1
     - 1
   * - infra.hw.cpu.cfg.002
     - Minimum Number of cores per CPU
     - This determines the minimum number of cores needed per CPU.
     - 20
     - 20
     - 1
     - 1
   * - infra.hw.cpu.cfg.003
     - NUMA alignment
     - NUMA alignment support and BIOS configured to enable NUMA.
     - N
     - Y
     - N
     - Y (*)

**Table 8-8:** TEC exceptions to infrastructure profile features and requirements

* This is immaterial if the number of CPU sockets (infra.hw.cpu.cfg.001) is 1.

.. note::
  None of the listed parameters forms part of a typical OpenStack flavour, except that the vCPU and memory requirements
  of a flavour cannot exceed the available hardware capacity.

Telco Edge Cloud: platform services deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section characterises the hardware capabilities for different edge deployments and the platform services that run
on the infrastructure.

.. note::
  The platform services are containerised to save resources, and benefit from intrinsic availability and autoscaling
  capabilities.

Platform services are:

- Identity
- Image
- Placement
- Compute
- Networking
- Message Queue
- DB Server

Storage services are:

- Ephemeral
- Persistent Block
- Persistent Object

Network services are:

- Management
- Underlay (Provider)
- Overlay


.. list-table:: Characteristics of infrastructure nodes
   :widths: 20 20 5 5 5 5 5 5 5 5 5 5 5 5 
   :header-rows: 1

   * - Node type
     - Identity
     - Image
     - Placement
     - Compute
     - Networking
     - Message Queue
     - DB Server
     - Ephemeral
     - Persistent Block
     - Persistent Object
     - Management
     - Underlay (Provider)
     - Overlay
   * - Control nodes
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - 
     - ✅
     - 
     - ✅
     - ✅
     - ✅
   * - Workload nodes (Compute)
     - 
     - 
     - 
     - ✅
     - ✅
     - 
     - 
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅
   * - Storage nodes
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - 
     - ✅
     - ✅
     - ✅
     - ✅
     - ✅

**Table 8-9:** Characteristics of infrastructure nodes

Depending on the facility capabilities, deployments at the edge may be similar to one of the following:

-  Small footprint edge device.
-  Single server: deploying multiple (one or more) workloads.
-  Single server: single controller and multiple (one or more) workloads.
-  HA at the edge (at least two edge servers): multiple controllers and multiple workloads.

Comparison of deployment topologies and edge terms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Profile extensions
   :widths: 10 10 10 10 10 10 10 10 10 10 10 10 10 10
   :header-rows: 1

   * - This Specification
     - Compute
     - Storage
     - Networking
     - RTT
     - Security
     - Scalability
     - Elasticity
     - Resiliency
     - Preferred Workload Architecture
     - Upgrades
     - OpenStack
     - OPNFV Edge
     - Edge Glossary
   * - Regional Data Centre (DC), Fixed
     - 1000's, Standardised, >1 CPU >20 cores / CPU
     - 10's EB, Standardised, HDD and NVMe, Permanence
     - >100 Gbps, Standardised
     - ~100 ms
     - Highly Secure
     - Horizontal and unlimited scaling
     - Rapid spin up and down
     - Infrastructure architected for resiliency, Redundancy for FT and HA
     - Microservices based, Stateless, Hosted on Containers
     - Firmware: When required, Platform SW: CD
     - Central Data Center
     - 
     - 
   * - Metro Data Centres, Fixed
     - 10's to 100's, Standardised, >1 CPU >20 cores / CPU
     - 100's PB, Standardised, NVMe on PCIe, Permanence
     - > 100 Gbps, Standardised
     - ~10 ms
     - Highly Secure
     - Horizontal but limited scaling
     - Rapid spin up and down
     - Infrastructure architected for some level of resiliency, Redundancy for limited FT and HA
     - Microservices based, Stateless, Hosted on Containers
     - Firmware: When required, Platform SW: CD
     - Edge Site
     - Large Edge
     - Aggregation Edge
   * - Edge, Fixed / Mobile
     - 10's, Some Variability, >=1 CPU, >10 cores / CPU
     - 100 TB, Standardised, NVMe on PCIe, Permanence / Ephemeral
     - 50 Gbps, Standardised
     - ~5 ms
     - Low Level of Trust
     - Horizontal but highly constrained scaling, if any
     - Rapid spin up (when possible) and down
     - Applications designed for resiliency against infra failures No or highly limited redundancy
     - Microservices based, Stateless, Hosted on Containers
     - Firmware: When required, Platform SW: CD
     - Far Edge Site
     - Medium Edge
     - Access Edge / Aggregation Edge
   * - Mini / Micro Edge, Mobil / Fixed
     - 1's, High Variability, Harsh Environments, 1 CPU >2 cores / CPU
     - 10's GB, NVMe, Ephemeral, Caching
     - 10 Gbps, Connectivity not Guaranteed
     - <2 ms Located in network proximity of EUD / IoT
     - Untrusted
     - Limited  Vertical Scaling (resizing)
     - Constrained
     - Applications designed for resiliency against infra failures No or highly limited redundancy
     - Microervices based or monolithic, Stateless or Stateful, Hosted on Containers or VMs, Subject to QoS, adaptive to
       resource availability, viz. reduce resource consumption as they saturate
     - Platform
     - Fog Computing (Mostly deprecated terminology), Extreme Edge, Far Edge
     - Small Edge
     - Access Edge

**Table 8-10:** Comparison of Deployment Topologies

O-RAN alignment and interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O-RAN is an operator led alliance group with members from the major Telco Operators, Vendors, and other interested ecosystem participants around the specification of Open Radio Access Networks. Its task is to cloudify the 3GPP specified RAN Network Functionalities with multi-vendor open interfaces in between the Network Functions, the Cloud Infrastructure, and the management. The Service Management and Orchestration (SMO) of multiple O-Clouds is also specified including a framework for 3rd party applications (rApps). There are also a few other open interfaces that are aimed to be specified e.g., for Radio Layer 1 HW Accelerators and some low-level Radio functions.

The O-RAN architecture is built up by a set of individual O-Clouds that provide the execution platforms for the Cloudified RAN Network Functions in a similar way as the Anuket NFVI infrastructure, although with O-RAN specified management interfaces. Each O-Cloud can be distributed on a set of Cloud Sites where they can provision VM and Container Node Clusters. The provisioning of O-Clouds and their resources are managed and orchestrated from a centralized RAN Service Management and Orchestration framework (SMO) over the O-RAN specified O2 interface like any other Telco Operations Support Systems (OSS).

On a high-level O-RAN covers similar specification grounds as what Anuket do, but there are some noteworthy differences both on specification level and on the aim for how O-Clouds are realized. O-RAN specifies how management and orchestration of the Network Functions and Cloud Infrastructure shall be done with a set of internal Services that also have a set of interface specifications for how the rApps could enhance the management functionality. O-RAN have also articulated that O-Clouds can be distributed over multiple Cloud Sites that are stitched over an externally specified WAN interconnect transport that is not part of the O-RAN.

.. figure:: ../figures/RM-Ch08-O-RAN_mappedon_Anuket-Image-1.png
   :name: O-RAN architecture mapped onto Anuket Reference Model
   :alt: O-RAN architecture mapped onto Anuket Reference Model

   O-RAN architecture mapped onto Anuket Reference Model

O-Clouds are in some ways similar to the Anuket Cloud Infrastructure with the notable differences that they have an O-RAN specified interface of how the O-Cloud infrastructure is managed (O2ims) and how workloads (e.g., whole or parts of Network Functions) are deployed on the O-Cloud clusters (O2dms). On a more detailed level the O-Clouds are internally very Layer2 (Ethernet) centric, today with strict requirements of determinism and low latency for Cloud Site internal connectivity in between the Network Functions. The O-Clouds also have the set of O-RAN specified HW Accelerators and an Acceleration Adaptation Layer (AAL) of how they are used from the Network Functions for their Radio-near functions.

A potential alignment between Anuket and O-RAN's O-Cloud specifications can be investigated. This would require an
analysis how an Anuket Reference Architecture based on open-source technology can support the O-RAN HW Accelerators and
a Layer2-centric networking infrastructure. It would enable the operators to have an internal Telco Cloud that supports
both Core and RAN Network Functions, and in the extension possibly also other workloads in a shared Cloud that supports
required Telco features and characteristics.

.. figure:: ../figures/RM-Ch08-Anuket_as_undercloud_O-RAN-Image-1.png
   :name: Anuket as potential under-cloud to O-Clouds in O-RAN
   :alt: Anuket as potential under-cloud to O-Clouds in O-RAN

   Anuket as potential under-cloud to O-Clouds in O-RAN
