# ``WKInternalsNotes/WKTextInteractionWrapper/selectionChanged()``

選択変更を通知する。

## Objective-C Declaration
```objective-c
- (void)selectionChanged;
```

## Discussion
`_textInteractionAssistant selectionChanged` を呼び出す。`USE(BROWSERENGINEKIT)` の場合は keyboard UI を更新し、`_showEditMenuAfterNextSelectionChange` が立っていれば 0.2 秒後に edit menu を表示するタイマーを設定する。

## References
- [`WKTextInteractionWrapper.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L43)
- [`WKTextInteractionWrapper.mm#L312`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L312)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
