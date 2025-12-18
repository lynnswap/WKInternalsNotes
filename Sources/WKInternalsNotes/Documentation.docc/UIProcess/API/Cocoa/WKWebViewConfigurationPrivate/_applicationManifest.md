# ``WKInternalsNotes/WKWebViewConfiguration/_applicationManifest``

WebPage 作成時に Application Manifest を固定で渡す

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setApplicationManifest:) _WKApplicationManifest *_applicationManifest WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: Application Manifest は設定されず、WebPage 作成パラメータへ渡されない（`nil`）。
- `_applicationManifest` を設定すると: manifest が WebPage 作成パラメータへ取り込まれ、Web content process 側へ渡される。
- `nil` に戻すと: manifest の設定を解除する。

## Details
- `ENABLE(APPLICATION_MANIFEST)` のみ

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L93)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1239`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1239)
- [`Source/WebKit/UIProcess/WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)
- [`Source/WebKit/WebProcess/WebPage/WebPage.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/WebProcess/WebPage/WebPage.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
