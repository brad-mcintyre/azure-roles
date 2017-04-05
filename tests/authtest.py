from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource.resources.resource_management_client import ResourceManagementClient

azure_credentials = ServicePrincipalCredentials(client_id="6b1400c3-5187-49af-a87c-d2ab9bda657c",
                                                secret="U8pm17n2VwbcTJk8FkeqDoILDHjPlyH7gorINdJgXjE=",
                                                tenant="dbc218fd-b8f5-4a62-9f50-b698b859feec")

subscription_id = "321a0e15-f849-4a60-bc00-31a7f21a45bb"
print ResourceManagementClient(azure_credentials,
                               subscription_id).providers.register("Microsoft.Compute")
