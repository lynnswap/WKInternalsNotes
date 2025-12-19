# ``WKInternalsNotes/WKContentView/_shouldUseContextMenus``

コンテキストメニューを使うべきかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldUseContextMenus;
```

## Default Value
`USE(UICONTEXTMENU)` 有効時は `SDKAlignedBehavior::HasUIContextMenuInteraction` の判定結果、無効時は `NO`。

## Discussion
SDK アラインメントの条件に応じて `UIContextMenu` を利用するかを決める。

## References
- [`WKContentViewInteraction.h#L939`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L939)
- [`WKContentViewInteraction.mm#L10205`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10205)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
