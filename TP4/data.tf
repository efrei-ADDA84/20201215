data "azurerm_resource_group" "main_resource_group" {
  name = var.azure_resource_group_name
}

data "azurerm_virtual_network" "main_virtual_network" {
  name                = var.network_name
  resource_group_name = var.azure_resource_group_name
}

data "azurerm_subnet" "internal" {
  name                 = var.subnet
  resource_group_name  = var.azure_resource_group_name
  virtual_network_name = data.azurerm_virtual_network.main_virtual_network.name
}