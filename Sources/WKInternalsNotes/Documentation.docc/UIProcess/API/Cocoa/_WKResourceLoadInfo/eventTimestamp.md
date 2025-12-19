# ``WKInternalsNotes/_WKResourceLoadInfo/eventTimestamp``

リソース読み込みのタイムスタンプを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSDate *eventTimestamp;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
内部の `eventTimestamp` を UNIX 時刻秒として `NSDate` に変換して返す。

## References
- [`_WKResourceLoadInfo.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L62)
- [`_WKResourceLoadInfo.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L123)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
