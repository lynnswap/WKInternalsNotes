# ``WKInternalsNotes/WKPreferencesPrivate/_extensibleSSOEnabled``

Extensible SSO を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=_isExtensibleSSOEnabled, setter=_setExtensibleSSOEnabled:) BOOL _extensibleSSOEnabled WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_extensibleSSOEnabled = YES`: `WebPageProxy::decidePolicyForNavigationAction` が `navigationAction->unsetShouldPerformSOAuthorization()` を呼ばず、SOAuthorization を抑制しない。
- `_extensibleSSOEnabled = NO`: `WebPageProxy::decidePolicyForNavigationAction` で `navigationAction->unsetShouldPerformSOAuthorization()` が実行され、SOAuthorization が抑制される。
- Implementation: [[[`Source/WebKit/UIProcess/WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)

## Details
- WebPreferences key: `ExtensibleSSOEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L177`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L177)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm)
- [`Source/WebKit/UIProcess/WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2849`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2849) (key: `ExtensibleSSOEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
