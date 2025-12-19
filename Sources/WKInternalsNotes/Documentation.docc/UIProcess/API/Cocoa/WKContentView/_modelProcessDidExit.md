# ``WKInternalsNotes/WKContentView/_modelProcessDidExit()``

Model プロセス終了時の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_modelProcessDidExit;
```

## Discussion
可視性伝播ビューを Model プロセスから切り離す。

## References
- [`WKContentView.h#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L103)
- [`WKContentView.mm#L925`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L925)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
