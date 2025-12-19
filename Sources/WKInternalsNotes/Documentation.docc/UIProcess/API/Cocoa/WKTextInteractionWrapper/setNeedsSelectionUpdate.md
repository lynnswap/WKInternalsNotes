# ``WKInternalsNotes/WKTextInteractionWrapper/setNeedsSelectionUpdate()``

選択表示の更新を要求する。

## Objective-C Declaration
```objective-c
- (void)setNeedsSelectionUpdate;
```

## Discussion
`HAVE(UI_TEXT_SELECTION_DISPLAY_INTERACTION)` の場合のみ `textSelectionDisplayInteraction` に `setNeedsSelectionUpdate` を呼び出す。

## References
- [`WKTextInteractionWrapper.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L59)
- [`WKTextInteractionWrapper.mm#L285`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L285)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
