# ``WKInternalsNotes/WKTextInteractionWrapper/deactivateSelection()``

テキスト選択表示を無効化する。

## Objective-C Declaration
```objective-c
- (void)deactivateSelection;
```

## Discussion
`USE(BROWSERENGINEKIT)` の場合は `textSelectionDisplayInteraction.activated = NO` を設定し、edit menu 表示用のフラグとタイマーも解除する。通常は `UIWKTextInteractionAssistant` に委譲する。

## References
- [`WKTextInteractionWrapper.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L41)
- [`WKTextInteractionWrapper.mm#L301`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L301)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
