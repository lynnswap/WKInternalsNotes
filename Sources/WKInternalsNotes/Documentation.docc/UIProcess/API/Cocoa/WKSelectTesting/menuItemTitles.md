# ``WKInternalsNotes/WKSelectTesting/menuItemTitles()``

コンテキストメニューの項目タイトル一覧を返す。

## Objective-C Declaration
```objective-c
- (NSArray<NSString *> *)menuItemTitles;
```

## Discussion
`USE(UICONTEXTMENU)` の場合に `UIMenu` の子要素からタイトルを抽出し、未対応の場合は `nil` を返す。

## References
- [`WKFormSelectPicker.mm#L758`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectPicker.mm#L758)
- [`WKFormSelectControl.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.h#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
