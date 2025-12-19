# ``WKInternalsNotes/WKContentView/_shouldUseContextMenusForFormControls``

フォームコントロールでコンテキストメニューを使うかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldUseContextMenusForFormControls;
```

## Default Value
`_formControlRefreshEnabled` と `_shouldUseContextMenus` の論理積。

## Discussion
フォームコントロールの更新が可能で、かつコンテキストメニューが有効な場合のみ `YES`。

## References
- [`WKContentViewInteraction.h#L940`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L940)
- [`WKContentViewInteraction.mm#L10213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10213)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
