# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_visitedLinkStore``

visited link 状態の共有/分離単位となる store を指定する

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, setter=_setVisitedLinkStore:) _WKVisitedLinkStore *_visitedLinkStore;
```

## Default Value
iOS: `default (lazy)` / macOS: `default (lazy)`

## Discussion
- この API を使わない場合: default store が lazy 生成され、その store に基づいて visited link 状態が管理される。
- `_visitedLinkStore` を設定すると: 指定した store が `pageConfiguration.visitedLinkStore` として使われ、visited link 状態の共有/分離の単位を制御できる。
- `nil` に戻すと: default store に戻る。

## Details
- getter で default store を生成

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L62)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L555`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L555)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L740`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L740)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
