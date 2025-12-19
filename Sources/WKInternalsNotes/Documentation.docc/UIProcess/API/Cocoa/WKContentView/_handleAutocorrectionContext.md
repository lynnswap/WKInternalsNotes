# ``WKInternalsNotes/WKContentView/_handleAutocorrectionContext(_:)``

自動補正コンテキストの更新を反映する。

## Objective-C Declaration
```objective-c
- (void)_handleAutocorrectionContext:(const WebKit::WebAutocorrectionContext&)context;
```

## Discussion
最新の自動補正コンテキストを保存し、必要ならソフトキーボード抑制解除を試みる。

## References
- [`WKContentViewInteraction.h#L921`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L921)
- [`WKContentViewInteraction.mm#L6088`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6088)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
