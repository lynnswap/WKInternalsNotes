# ``WKInternalsNotes/WKContentView/_writePromisedAttachmentToPasteboard(_:)``

添付ファイルをペーストボードに書き込む。

## Objective-C Declaration
```objective-c
- (void)_writePromisedAttachmentToPasteboard:(WebCore::PromisedAttachmentInfo&&)info;
```

## Discussion
対応プラットフォームでは `ItemProvider` を作成し、data owner を設定してペーストボードへ登録する。watchOS/Apple TV では no-op。

## References
- [`WKContentViewInteraction.h#L964`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L964)
- [`WKContentViewInteraction.mm#L12514`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12514)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
