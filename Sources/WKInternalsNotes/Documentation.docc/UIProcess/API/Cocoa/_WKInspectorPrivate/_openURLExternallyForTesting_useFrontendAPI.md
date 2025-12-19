# ``WKInternalsNotes/_WKInspector/_openURLExternallyForTesting(_:useFrontendAPI:)``

外部 URL オープンをテスト用にフロントエンド API またはナビゲーションで再現する。

## Objective-C Declaration
```objective-c
- (void)_openURLExternallyForTesting:(NSURL *)url useFrontendAPI:(BOOL)useFrontendAPI;
```

## Discussion
`useFrontendAPI` が `YES` の場合は `InspectorFrontendHost.openURLExternally(...)` を `evaluateInFrontendForTesting` で実行する。`NO` の場合は `inspectorWebView` に request を load し、内部 NavigationDelegate 経由で処理させる。

## References
- [`_WKInspectorPrivateForTesting.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorPrivateForTesting.h#L30)
- [`_WKInspectorTesting.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorTesting.mm#L59)
- [`_WKInspectorTesting.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorTesting.mm#L59)
- [`_WKInspectorTesting.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorTesting.mm#L59)
- [`WebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
