# ``WKInternalsNotes``

## Overview
- Baseline WebKit revision: [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9)
このモジュールは WebKit の UIProcess で使われる Objective-C API（公開/非公開を含む）の調査メモです。
Swift-DocC のシンボルページとして読めるように、WebKit のソース（`Source/WebKit/UIProcess/`）から合成した symbol graph を同梱しています。
各型のページでは Objective-C category 名（例: `WKPrivate`）ごとにメンバーを整理し、個別ページで挙動/既定値/参照（WebKit のパス）を追跡します。

## Topics

### Types
WebKit UIProcess に登場する型（class/protocol など）の一覧。

#### Classes
- ``WKInternalsNotes/_WKInspector``
- ``WKInternalsNotes/_WKRemoteWebInspectorViewController``
- ``WKInternalsNotes/_WKUserContentExtensionStore``
- ``WKInternalsNotes/_WKUserContentFilter``
- ``WKInternalsNotes/WKBackForwardList``
- ``WKInternalsNotes/WKBackForwardListItem``
- ``WKInternalsNotes/WKContentRuleList``
- ``WKInternalsNotes/WKContentRuleListStore``
- ``WKInternalsNotes/WKContentWorld``
- ``WKInternalsNotes/WKContextMenuElementInfo``
- ``WKInternalsNotes/WKFrameInfo``
- ``WKInternalsNotes/WKHTTPCookieStore``
- ``WKInternalsNotes/WKNavigation``
- ``WKInternalsNotes/WKNavigationAction``
- ``WKInternalsNotes/WKNavigationResponse``
- ``WKInternalsNotes/WKOpenPanelParameters``
- ``WKInternalsNotes/WKPreferences``
- ``WKInternalsNotes/WKProcessPool``
- ``WKInternalsNotes/WKSecurityOrigin``
- ``WKInternalsNotes/WKSnapshotConfiguration``
- ``WKInternalsNotes/WKUserContentController``
- ``WKInternalsNotes/WKUserScript``
- ``WKInternalsNotes/WKView``
- ``WKInternalsNotes/WKWebExtension``
- ``WKInternalsNotes/WKWebExtensionAction``
- ``WKInternalsNotes/WKWebExtensionCommand``
- ``WKInternalsNotes/WKWebExtensionContext``
- ``WKInternalsNotes/WKWebExtensionController``
- ``WKInternalsNotes/WKWebExtensionControllerConfiguration``
- ``WKInternalsNotes/WKWebExtensionDataRecord``
- ``WKInternalsNotes/WKWebExtensionMatchPattern``
- ``WKInternalsNotes/WKWebExtensionMessagePort``
- ``WKInternalsNotes/WKWebpagePreferences``
- ``WKInternalsNotes/WKWebsiteDataRecord``
- ``WKInternalsNotes/WKWebsiteDataStore``
- ``WKInternalsNotes/WKWebView``
- ``WKInternalsNotes/WKWebViewConfiguration``
- ``WKInternalsNotes/WKWindowFeatures``

#### Protocols
- ``WKInternalsNotes/WKBrowsingContextLoadDelegatePrivate``
- ``WKInternalsNotes/WKDownloadDelegatePrivate``
- ``WKInternalsNotes/WKHistoryDelegatePrivate``
- ``WKInternalsNotes/WKNavigationDelegatePrivate``
- ``WKInternalsNotes/WKUIDelegatePrivate``
- ``WKInternalsNotes/WKURLSchemeTaskPrivate``
- ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate``
