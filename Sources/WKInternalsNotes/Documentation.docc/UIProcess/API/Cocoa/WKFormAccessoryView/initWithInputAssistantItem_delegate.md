# ``WKInternalsNotes/WKFormAccessoryView/initWithInputAssistantItem(_:delegate:)``

入力補助ビューを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithInputAssistantItem:(UITextInputAssistantItem *)inputAssistantItem delegate:(id<WKFormAccessoryViewDelegate>)delegate;
```

## Discussion
delegate を保存し、画面サイズに応じてユニバーサルコントロールバーまたは左右ツールバー構成を作成する。

## References
- [`WKFormAccessoryView.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.h#L48)
- [`WKFormAccessoryView.mm#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormAccessoryView.mm#L156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
