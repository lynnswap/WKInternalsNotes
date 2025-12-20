# ``WKInternalsNotes/WKFormSelectControl/menuItemTitles``

選択肢のタイトル一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<NSString *> *menuItemTitles;
```

## Discussion
`control` が `menuItemTitles` に応答できる場合のみ `WKSelectTesting` として取得し、応答できない場合は `nil` を返す。

## References
- [`WKFormSelectControl.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.h#L46)
- [`WKFormSelectControl.mm#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L122)
- [`WKFormSelectControl.mm#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFormSelectControl.mm#L124)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
