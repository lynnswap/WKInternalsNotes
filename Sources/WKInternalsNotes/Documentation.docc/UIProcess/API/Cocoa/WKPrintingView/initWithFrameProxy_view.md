# ``WKInternalsNotes/WKPrintingView/initWithFrameProxy(_:view:)``

`WebFrameProxy` と `wkView` を保持して初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithFrameProxy:(WebKit::WebFrameProxy&)frame view:(NSView *)wkView;
```

## Discussion
`[super init]` 後に `lazyInitialize(_webFrame, Ref { frame })` を行い、`_wkView` に `wkView` を設定する。

## References
- [`WKPrintingView.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKPrintingView.h#L76)
- [`WKPrintingView.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKPrintingView.mm#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
