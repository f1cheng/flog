<template>
  <div id='deco'>
     <div class='ShowLevel'>
       <el-breadcrumb seperator="/" class="padding-b">
          <el-breadcrumb-item :to="{path: '/'}">Home</el-breadcrumb-item>
          <el-breadcrumb-item>Decoration</el-breadcrumb-item>
       </el-breadcrumb>
     </div>
     <div class='ToSearch' font-size:0>
       <table class="tables">
       <td><el-col><el-input placeholder="项目名" v-model="SearchData.name" style="display:inline"></el-input></el-col></td>
       <td><el-col><el-button type="button" plain @click="on_search">搜索</el-button></el-col></td>
       </table>
     </div>
     <div class="ToInput">
       <table class="tables">
         <tr>
           <td><el-col width="15%"><el-input placeholder="编号" v-model="InData.payid"></el-input></el-col></td>
           <td><el-col width="15%"><el-input placeholder="项目名" v-model="InData.name"></el-input></el-col></td>
           <td><el-col width="15%"><el-input placeholder="费用" v-model="InData.fee"></el-input></el-col><td>
           <td><el-date-picker v-model="InData.paydate" type="datetime" placeholder="chosse time" value-format="yyyy-MM-dd HH:mm:ss"></el-date-picker></td>
           <td><el-col width="15%"><el-button type="button" plain @click.native="on_add">添加</el-button></el-col></td>
         </tr>
       </table>
     </div>
    <div class='Listing'>
       <el-table :data="ItemsFee.slice((currentPage-1)*pagesize, currentPage*pagesize)" ref="multipleTable" border show-summary :header-cell-style="tableHeaderColor">
         <!--<el-table-column type="selection" width="55"></el-table-column>-->
         <el-table-column prop="payid" label="编号" width="80">
           <template slot-scope="scope">
              <span>{{scope.row.payid}}</span>
           </template>
         </el-table-column>
         <el-table-column prop="name" label="项目" width="140">
           <template slot-scope="{row, $index}">
              <input class="edit-cell" v-if="showEdit[$index]" v-model="row.name">
              <span v-if="!showEdit[$index]">{{row.name}}</span>
           </template>
         </el-table-column>
         <el-table-column prop="fee" label="费用" width="120">
           <template slot-scope="{row, $index}">
              <input class="edit-cell" v-if="showEdit[$index]" v-model="row.fee">
              <span v-if="!showEdit[$index]">{{row.fee}}</span>
           </template>
         </el-table-column>
         <el-table-column prop="paydate" label="付款时间" width="200">
           <template slot-scope="{row, $index}">
              <!--<input class="edit-cell" v-if="showEdit[$index]" v-model="row.paydate">-->
              <el-date-picker v-if="showEdit[$index]" v-model="row.paydate" type="datetime" value-format="yyyy-MM-dd HH:mm:ss"></el-date-picker>
              <span v-if="!showEdit[$index]">{{row.paydate}}</span>
           </template>
         </el-table-column>
         <el-table-column label="操作" width="200">
           <template slot-scope="scope">
           <el-button size="small" type="danger" @click="handle_edit(scope.$index, scope.row)" v-if="!showBtn[scope.$index]">编辑</el-button>
           <el-button size="small" type="danger" @click="handle_save(scope.$index, scope.row)" v-if="showBtn[scope.$index]">保存</el-button>
           <el-button size="mini" type="info" @click.native="handle_delete(scope.$index, scope.row)">删除</el-button>
           </template>
         </el-table-column>
       </el-table>
     </div>
     <div style="text-align: left;margin-top: 5px;">
       <el-pagination
          background
          layout="prev, pager, next"
          :page-size="pagesize" :total="totalSize"
          @size-change="handleSizeChange"
          @current-change="current_change">
      </el-pagination>
    </div>
    <div class="SSum">Total Fee (RMB): {{ sumFee }}
      <!--<input v-model="sumFee" placeholder="edit me">-->
    </div>    
   </div>
</template>

<script>
export default {
  name: 'ItemsFeeA',
  data () {
    return { ItemsFee: [],
      InData: {},
      SearchData: {},
      showEdit: [],
      showBtn: [],
      currentPage: 1,
      pagesize: 6,
      totalSize: 0,
      sumFee: 0 
    }
  },
  mounted: function () {
    this.$axios({
      url: 'decoration/cart/',
      method: 'get',
      params: {}
    }).then(res => {
      res = res.data
      this.ItemsFee = res.data
      this.totalSize = this.ItemsFee.length
      //alert(this.ItemsFee[0].name)
      //alert(res.status)
      //alert(this.sumFee)
      this.sumFee = this.calc_sum(this.ItemsFee)
    })
  },
  methods: {
    tableRowStyle ({ row, rowIndex }) {
      return 'background-color: #F7F6Fd'
    },
    tableHeaderColor ({row, column, rowIndex, columnIndex}) {
      if (rowIndex === 0) {
        return 'background-color: lightblue;color: #fff;font-weight: 500;'
      }
    },
    calc_sum: function(fees) {
      var total = 0
      for (var i=0; i < fees.length; i++) {
        total = parseInt(fees[i].fee) + total
      }
      return total
    },
    on_add () {
      this.$axios({
        url: 'decoration/cart/',
        method: 'post',
        data: {
          payid: this.InData.payid,
          name: this.InData.name,
          fee: this.InData.fee,
          paydate: this.InData.paydate
        }
      }).then(res => {
        res = res.data.data
        //this.ItemsFee.append(res[0])
        this.ItemsFee.push(res[0])
        //this.ItemsFee.splice(this.totalSize, 0, res)
        this.totalSize = this.ItemsFee.length
        this.sumFee = this.calc_sum(this.ItemsFee)
        //alert(this.sumFee)
        //alert(res.msg)
        //requery()
      })
      this.InData.payid = ''
      this.InData.name = ''
      this.InData.fee = ''
      this.InData.paydate = ''
      //this.$nextTick(() => {this.$refs.multipleTable.doLayout(); this.sumFee = 32})
      //this.$forceUpdate()
      //this.keyItem = Math.random()
      //this.keyItem = Math.random()
    },
    on_search () {
      this.$axios({
        url: 'decoration/cart/',
        method: 'get',
        params: {
          name: this.SearchData.name
        }
      }).then(res => {
        res = res.data
        this.ItemsFee = res.data
        this.totalSize = this.ItemsFee.length
        this.currentPage = 1
        this.sumFee = this.calc_sum(this.ItemsFee)
        //alert(this.sumFee)
        //alert(this.totalSize)
        //alert(this.currentPage)
      })
    },
    handle_delete (index, row) {
      //this.ItemsFee.splice(index, 1)
      this.$axios({
        url: 'decoration/cart/',
        method: 'delete',
        data: {
          payid: row.payid,
          name: row.name,
          fee: row.fee,
          paydate: row.paydate
        }
      }).then(res => {
        //res = res.data
        //requery()
        //alert(this.currentPage)
        let id = (this.currentPage-1)*this.pagesize+index
        //alert(id)
        this.ItemsFee.splice(id, 1)
        this.totalSize = this.totalSize - 1
        this.currentPage = 1
        this.sumFee = this.calc_sum(this.ItemsFee)
        //alert(this.sumFee)
        this.$nextTick(() => {this.$refs.multipleTable.doLayout();})
      })
      //this.$set(this.ItemsFee,index,row)
    },
    handle_edit (index, row) {
      this.showEdit[index] = true
      this.showBtn[index] = true
      this.$set(this.showEdit, row, true)
      this.$set(this.showBtn, row, true)
      this.$nextTick(() => {this.$refs.multipleTable.doLayout();})
    },
    handle_save (index, row) {
      this.showEdit[index] = false
      this.showBtn[index] = false
      //this.$set(this.showEdit, row, false)
      //this.$set(this.showBtn, row, false)
      this.$axios({
        url: 'decoration/cart/',
        method: 'put',
        data: {
          payid: row.payid,
          name: row.name,
          fee: row.fee,
          paydate: row.paydate
        }
      }).then(res => {
        //res = res.data
        //this.ItemsFee = res.data
        //alert(res.msg)
        //todo
        this.sumFee = this.calc_sum(this.ItemsFee)
        this.$nextTick(() => {this.$refs.multipleTable.doLayout();})
        //requery()
      })
    },
    current_change (currentPage) {
      this.currentPage = currentPage
    },
    handleSizeChange (newSize) {
      this.pagesize = newSize
    }
  }
}
</script>

<style>
.el-breadcrumb {
  display: inline-block;
}

.el-table__header tr,
  .el-table__header th {
      padding: 0;
      height: 30px;
      line-height: 30px;
  }
.el-table__body tr,
  .el-table__body td {
      padding: 0;
      height: 20px;
      line-height: 20px;
  }
#sum1 {
      padding: 0;
      height: 20px;
      line-height: 20px;
  }
#tofill {
      padding: 0;
      height: 20px;
      line-height: 20px;
  }
</style>
