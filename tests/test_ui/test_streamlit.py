import pytest
import streamlit as st
from unittest.mock import patch, MagicMock
import importlib
import sys

def test_frontend_app_imports():
    """Frontend 앱 임포트 테스트"""
    try:
        import frontend.app
        assert True
    except ImportError:
        pytest.fail("Frontend 앱 임포트 실패")

def test_session_manager_import():
    """SessionManager 임포트 테스트"""
    try:
        from frontend.utils.session_manager import SessionManager
        session_manager = SessionManager()
        assert session_manager is not None
    except ImportError:
        pytest.fail("SessionManager 임포트 실패")

def test_chat_interface_import():
    """ChatInterface 임포트 테스트"""
    try:
        from frontend.components.chat_interface import ChatInterface
        from frontend.utils.session_manager import SessionManager
        
        session_manager = SessionManager()
        chat_interface = ChatInterface(session_manager)
        assert chat_interface is not None
    except ImportError:
        pytest.fail("ChatInterface 임포트 실패")

def test_product_card_import():
    """ProductCard 임포트 테스트"""
    try:
        from frontend.components.product_card import ProductCard
        product_card = ProductCard()
        assert product_card is not None
    except ImportError:
        pytest.fail("ProductCard 임포트 실패")

def test_api_client_import():
    """APIClient 임포트 테스트"""
    try:
        from frontend.utils.api_client import APIClient
        api_client = APIClient()
        assert api_client is not None
    except ImportError:
        pytest.fail("APIClient 임포트 실패")

@patch('streamlit.set_page_config')
def test_app_config(mock_config):
    """앱 설정 테스트"""
    try:
        # 이미 로드된 모듈을 제거하고 다시 로드
        if 'frontend.app' in sys.modules:
            del sys.modules['frontend.app']
        import frontend.app
        # 설정이 호출되었는지 확인
        mock_config.assert_called_once()
    except Exception as e:
        pytest.fail(f"앱 설정 테스트 실패: {str(e)}")

def test_config_settings():
    """설정 파일 테스트"""
    try:
        from frontend.config.settings import AppConfig, UIMessages, StyleConfig
        
        config = AppConfig()
        ui_messages = UIMessages()
        style_config = StyleConfig()
        
        assert config.PAGE_TITLE == "PriceFinder Agent"
        assert config.PAGE_ICON == "🛒"
        assert ui_messages.CHAT_INPUT_PLACEHOLDER is not None
        assert style_config.CHAT_CONTAINER_HEIGHT > 0
        
    except ImportError:
        pytest.fail("설정 파일 임포트 실패") 