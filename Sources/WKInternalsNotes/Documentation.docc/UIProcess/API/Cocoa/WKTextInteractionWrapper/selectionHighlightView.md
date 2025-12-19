# ``WKInternalsNotes/WKTextInteractionWrapper/selectionHighlightView``

選択ハイライトのビューを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIView *selectionHighlightView;
```

## Default Value
`HAVE(UI_TEXT_SELECTION_DISPLAY_INTERACTION)` でない場合は `nil`。

## Discussion
`textSelectionDisplayInteraction` の `highlightView` を返す。

## References
- [`WKTextInteractionWrapper.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L73)
- [`WKTextInteractionWrapper.mm#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L193)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
