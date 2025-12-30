# ``WKInternalsNotes/_WKElementAction/imageForElementActionType(_:)``

アクション種別に応じたアイコンを返す。

## Objective-C Declaration
```objective-c
+ (UIImage *)imageForElementActionType:(_WKElementActionType)actionType WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`USE(UICONTEXTMENU)` 環境では SF Symbols を種別ごとに割り当てる。`Custom` や `ToggleShowLinkPreviews` は `nil`、機能フラグ無効時の画像系は `nil` を返す。

## References
- [`_WKElementAction.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L74)
- [`_WKElementAction.mm#L278`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L278)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
