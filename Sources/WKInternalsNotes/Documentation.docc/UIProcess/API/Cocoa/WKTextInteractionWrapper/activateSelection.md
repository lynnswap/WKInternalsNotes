# ``WKInternalsNotes/WKTextInteractionWrapper/activateSelection()``

テキスト選択表示を有効化する。

## Objective-C Declaration
```objective-c
- (void)activateSelection;
```

## Discussion
`USE(BROWSERENGINEKIT)` の場合は `textSelectionDisplayInteraction.activated = YES` を設定し、それ以外は `UIWKTextInteractionAssistant` に委譲する。

## References
- [`WKTextInteractionWrapper.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L40)
- [`WKTextInteractionWrapper.mm#L292`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L292)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
