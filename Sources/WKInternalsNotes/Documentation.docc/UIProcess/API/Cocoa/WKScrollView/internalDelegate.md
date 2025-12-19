# ``WKInternalsNotes/WKScrollView/internalDelegate``

内部スクロール delegate を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign) WKWebView <WKBEScrollViewDelegate> *internalDelegate;
```

## Default Value
`nil`（設定されるまで未指定）。

## Discussion
setter で `_internalDelegate` を更新し、`_updateDelegate` を通じて delegate の配線を更新する。外部 delegate がある場合は forwarder を使って両方へ通知する。

## References
- [`WKScrollView.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L36)
- [`WKScrollView.mm#L203`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L203)
- [`WKScrollView.mm#L240`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L240)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
