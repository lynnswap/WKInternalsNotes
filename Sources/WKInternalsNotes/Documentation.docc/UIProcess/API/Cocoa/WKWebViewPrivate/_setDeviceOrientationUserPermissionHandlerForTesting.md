# ``WKInternalsNotes/WKWebView/_setDeviceOrientationUserPermissionHandlerForTesting(_:)``

`_setDeviceOrientationUserPermissionHandlerForTesting` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setDeviceOrientationUserPermissionHandlerForTesting:(BOOL (^)(void))handler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/ios/WKWebViewPrivateForTestingIOS.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewPrivateForTestingIOS.h#L84)
- [`API/ios/WKWebViewTestingIOS.mm#L438`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L438)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
