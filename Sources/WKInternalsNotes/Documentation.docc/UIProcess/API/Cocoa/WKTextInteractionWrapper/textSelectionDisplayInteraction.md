# ``WKInternalsNotes/WKTextInteractionWrapper/textSelectionDisplayInteraction``

選択表示用の `UITextSelectionDisplayInteraction` を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UITextSelectionDisplayInteraction *textSelectionDisplayInteraction;
```

## Default Value
見つからない場合は `nil`。

## Discussion
`USE(BROWSERENGINEKIT)` かつ `_asyncTextInteraction` がある場合はその `textSelectionDisplayInteraction` を返す。そうでなければ view の `interactions` を走査して `UITextSelectionDisplayInteraction` を探す。

## References
- [`WKTextInteractionWrapper.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L47)
- [`WKTextInteractionWrapper.mm#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L163)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
