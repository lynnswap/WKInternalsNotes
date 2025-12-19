# ``WKInternalsNotes/_WKInspector/_fetchURLForTesting(_:)``

インスペクタフロントエンドで `fetch()` を実行してリクエストを発生させるテスト用フック。

## Objective-C Declaration
```objective-c
- (void)_fetchURLForTesting:(NSURL *)url;
```

## Discussion
JavaScript の `fetch("<url>")` を `evaluateInFrontendForTesting` に渡して実行する。フロントエンドの `inspectorPage` が無い場合は評価されない。

## References
- [`_WKInspectorPrivateForTesting.h#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorPrivateForTesting.h#L29)
- [`_WKInspectorTesting.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorTesting.mm#L54)
- [`_WKInspectorTesting.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorTesting.mm#L54)
- [`WebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
