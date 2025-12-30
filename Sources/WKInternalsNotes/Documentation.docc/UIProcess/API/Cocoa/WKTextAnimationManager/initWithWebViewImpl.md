# ``WKInternalsNotes/WKTextAnimationManager/initWithWebViewImpl(_:)``

WebView とエフェクトビューを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithWebViewImpl:(WebKit::WebViewImpl&)view;
```

## Discussion
`_webView` を保持し、`_chunkToEffect` を初期化して `_effectView` を生成する。`_effectView` の `frame` を WebView の bounds に合わせる。

## References
- [`WKTextAnimationManagerMac.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.h#L42)
- [`WKTextAnimationManagerMac.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextAnimationManagerMac.mm#L76)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
