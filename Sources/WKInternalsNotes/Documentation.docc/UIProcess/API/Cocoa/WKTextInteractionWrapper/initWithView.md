# ``WKInternalsNotes/WKTextInteractionWrapper/initWithView(_:)``

`WKContentView` と紐付けてテキストインタラクションを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithView:(WKContentView *)contentView;
```

## Discussion
view を保存し、`view.shouldUseAsyncInteractions` が `true` なら `BETextInteraction` を生成して delegate 設定・view への追加まで行う。そうでなければ `UIWKTextInteractionAssistant` を生成する。Apple TV では `UIContextMenuInteraction` を取り外し、外部 delegate を解除する。

## References
- [`WKTextInteractionWrapper.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L38)
- [`WKTextInteractionWrapper.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L117)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
