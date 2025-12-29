# ``WKInternalsNotes/_WKTouchEventGenerator/sharedTouchEventGenerator()``

タッチイベント生成器のシングルトンを返す。

## Objective-C Declaration
```objective-c
+ (_WKTouchEventGenerator *)sharedTouchEventGenerator;
```

## Discussion
静的に確保した `_WKTouchEventGenerator` を返す。

## References
- [`_WKTouchEventGenerator.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.h#L38)
- [`_WKTouchEventGenerator.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTouchEventGenerator.mm#L101)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
