import requests
from unittest.mock import Mock

import unittest

from .permission import check_permission, _check_permission

class PermissionTests(unittest.TestCase):
    def test_check_permission1(self):
        result = _check_permission("condominium.residential:retrieve", [
            'condominium.residential[residentialId=9b5ad390-b255-47a0-859d-030a6e14f23e].vehicles:*',
            'condominium.residential:list'
        ], {})
        
        self.assertFalse(result)
        
    def test_check_permission2(self):
        result = _check_permission("condominium.residential:retrieve", [
            'condominium.residential[residentialId=9b5ad390-b255-47a0-859d-030a6e14f23e]:*',
            'condominium.residential:list'
        ], {
            "residentialId": "9b5ad390-b255-47a0-859d-030a6e14f23e"
        })
        
        self.assertTrue(result)
        
    def test_check_permission3(self):
        result = _check_permission("condominium.residential:update", [
            'condominium.residential:update[residentialId=9b5ad390-b255-47a0-859d-030a6e14f23e]',
            'condominium.residential:list'
        ], {
            "residentialId": "9b5ad390-b255-47a0-859d-030a6e14f23e"
        })
        
        self.assertTrue(result)
        
    def test_check_permission4(self):
        result = _check_permission("condominium.residential:update", [
            'condominium.*:*',
            'condominium.residential:list'
        ], {
            "residentialId": "9b5ad390-b255-47a0-859d-030a6e14f23e"
        })
        
        self.assertTrue(result)
        
    def test_check_permission5(self):
        result = _check_permission("condominium.residential:update", [
            'condominium.*:list',
            'condominium.*:retrieve',
            'condominium.residential:list'
        ], {
            "residentialId": "9b5ad390-b255-47a0-859d-030a6e14f23e"
        })
        
        self.assertFalse(result)
