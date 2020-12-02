from ..types import BucketName, DateTime
from .region import Region
from . import base
# from . import validation

import datetime

class Bucket(base.BaseModel):
    name: str
    region: Region
    arn: str
    creation_date: DateTime

    # @validation.validate_arguments
    def __init__ \
            (
                self,
                name: str,
                region: Region,
                creation_date: datetime.datetime,
            ):
        super().__init__ \
        (
            name          = str(BucketName(name)),
            region        = region,
            arn           = f'arn:aws:s3::{name!s}',
            creation_date = DateTime.fromdatetime(creation_date),
        )

    def __repr__(self):
        return super().__repr__ \
        (
            name   = self.name,
            region = self.region.code,
        )
