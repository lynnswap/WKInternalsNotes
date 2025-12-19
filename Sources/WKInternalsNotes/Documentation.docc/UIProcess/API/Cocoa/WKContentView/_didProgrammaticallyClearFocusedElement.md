# ``WKInternalsNotes/WKContentView/_didProgrammaticallyClearFocusedElement(_:)``

プログラム的にフォーカス解除された要素に対する後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didProgrammaticallyClearFocusedElement:(WebCore::ElementContext&&)context;
```

## Discussion
フォーカス中の要素と `context` が一致する場合にテキスト入力コンテキストを無効化する。

## References
- [`WKContentViewInteraction.h#L810`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L810)
- [`WKContentViewInteraction.mm#L8695`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8695)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
