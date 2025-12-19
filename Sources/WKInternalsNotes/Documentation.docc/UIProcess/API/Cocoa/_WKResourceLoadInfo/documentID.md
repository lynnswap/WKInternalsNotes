# ``WKInternalsNotes/_WKResourceLoadInfo/documentID``

ドキュメント識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSUUID *documentID;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
内部の `documentID` が存在する場合に `NSUUID` を生成して返し、無ければ `nil`。

## References
- [`_WKResourceLoadInfo.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L59)
- [`_WKResourceLoadInfo.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L106)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
