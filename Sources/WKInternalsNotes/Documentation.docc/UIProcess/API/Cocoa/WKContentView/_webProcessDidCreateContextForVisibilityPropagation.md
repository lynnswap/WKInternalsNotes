# ``WKInternalsNotes/WKContentView/_webProcessDidCreateContextForVisibilityPropagation()``

Web プロセスの可視性伝播コンテキスト生成を通知する。

## Objective-C Declaration
```objective-c
- (void)_webProcessDidCreateContextForVisibilityPropagation;
```

## Discussion
`_setupVisibilityPropagationForWebProcess` を呼び、伝播ビューを再設定する。

## References
- [`WKContentView.h#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L109)
- [`WKContentView.mm#L955`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L955)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
