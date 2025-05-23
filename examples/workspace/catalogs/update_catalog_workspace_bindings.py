import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

created = w.catalogs.create(name=f"sdk-{time.time_ns()}")

_ = w.catalogs.update(name=created.name, isolation_mode=catalog.CatalogIsolationMode.ISOLATED)

# cleanup
w.catalogs.delete(name=created.name, force=True)
