package com.actionml.authserver.dal

import com.actionml.authserver.model.Permission

import scala.concurrent.Future

trait PermissionDao {
  def findByBearerToken(token: String): Future[Iterable[Permission]]
}